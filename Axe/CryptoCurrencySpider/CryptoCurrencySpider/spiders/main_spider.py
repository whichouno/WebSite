import scrapy
from ..items import DataItem, HistoryItem
from dateutil import parser
import traceback

# from scrapy.crawler import CrawlerRunner, CrawlerProcess
# from twisted.internet import reactor
from scrapy.cmdline import execute

XPATH_ENTRY = {
    'coin_details': './td[2]/a/@href',
    'historical_data': '/html/body/div[2]/div/div[1]//a[contains(@href,"historical-data")]/@href',
}

XPATH_ELEMENT = {
    'coins_list': '//*[@id="currencies"]/tbody/tr',
    'rank': '/html/body/div[2]/div/div[1]//span[contains(text(),''Rank'')]/text()',
    'coin_fullname': '/html/body/div[2]/div/div[1]//h1[contains(@class,''name'')]/img//@alt',
    'coin_shortname': '/html/body/div[2]/div/div[1]//h1[contains(@class,''name'')]/span/text()',
    'historical_data': '//*[@id="historical-data"]/div/div[2]/table/tbody/tr',
}


# scrapy crawl K -s JOBDIR=cryptocurrency/coin_jobdir/
class MainSpider(scrapy.Spider):
    name = 'main'

    allowed_domains = ['coinmarketcap.com']
    # 默认访问地址参数
    start_urls = ['https://coinmarketcap.com']

    pre_item = None
    DICT_COIN = {}

    begin_date = "20130428"
    end_date = "20190501"
    category = ['bitcoin']
    # 1:批量解析 0:指定解析
    parse_type = 0

    # scrapy crawl coin -a begindate='20190501' -a enddate='20190503' -a category='bitcoin' -a parsetype=0
    # scrapy crawl coin -a begindate='20190501' -a enddate='20190503' -a category='bitcoin|ethereum|ethereum-classic|bitcoin-cash|BitShares|eos|neo|litecoin' -a parsetype=0
    def __init__(self, *args, **kwargs):
        self.begin_date = str(kwargs.get('begindate'))
        self.end_date = str(kwargs.get('enddate'))
        self.category = str(kwargs.get('category'))
        self.parse_type = int(kwargs.get('parsetype'))

        super(MainSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        print('parse:********************************')
        print(self.begin_date, self.end_date, self.category)
        try:
            if (self.parse_type == 1):
                coins = response.xpath(XPATH_ELEMENT['coins_list'])
                for each_coin in coins:
                    each_coin_details_url = response.urljoin(each_coin.xpath(XPATH_ENTRY['coin_details']).extract()[0])
                    each_coin_id = each_coin.xpath('./td[1]/text()').extract()[0].replace(" ", "").replace("\n", "")
                    yield scrapy.Request(each_coin_details_url, callback=self.each_coin_parse,
                                         meta={'id': each_coin_id})
            elif (self.parse_type == 0):
                urls = ['https://coinmarketcap.com/currencies/' + self.category]
                # for c in self.category:
                #     urls.append('https://coinmarketcap.com/currencies/' + c)

                for each_coin_href in urls:
                    yield scrapy.Request(each_coin_href, callback=self.each_coin_parse, meta={'id': -1})
            else:
                print("self.parse_type:", self.parse_type)
                print("PARSE_SWITCH ERR")
        except:
            filepath = "/Users/ouno/Projects/python/cryptocurrency/error_log/err.txt"
            with open(filepath, 'a+') as fp:
                traceback.print_exc(file=fp)

    def each_coin_parse(self, response):
        # 使用contains模糊查找，定位历史数据链接。ardor等的xpath会与其他币种有差异。
        # 正常：    //html/body/div[4]/div/div[1]/div[5]/div[1]/ul/li[5]/a/@href
        # ardor等： //html/body/div[4]/div/div[1]/div[6]/div[1]/ul/li[5]/a/@href
        # /html/body/div[2]/div/div[1]/div[5]/div[1]/ul/li[5]/a
        # history_data_url = response.urljoin(response.xpath('//html/body/div[4]/div/div[1]//a[contains(@href,"historical-data")]/@href').extract()[0])

        # 排名 : "Rank 2" /html/body/div[2]/div/div[1]/div[4]/ul/li[1]/span[2]
        id = response.meta['id']
        if id == -1:
            id = response.xpath(XPATH_ELEMENT['rank']).extract()[0].replace(" ", "").replace("Rank", "")

        history_data_url = response.urljoin(
            response.xpath(XPATH_ENTRY['historical_data']).extract()[0])

        yield scrapy.Request(history_data_url, callback=self.set_date_parse, meta={'id': id})

    def set_date_parse(self, response):
        set_date_url = response.urljoin("?start=" + self.begin_date + "&end=" + self.end_date + "")
        yield scrapy.Request(set_date_url, callback=self.history_data_parse, meta={'id': response.meta['id']})

    # 获取历史数据
    def history_data_parse(self, response):
        try:
            # //*[@id="historical-data"]/div/div[3]/table/tbody/tr
            history_data = response.xpath(XPATH_ELEMENT['historical_data'])

            for eachday_day in history_data:
                item = HistoryItem()
                # item['id'] : 9
                item['id'] = response.meta['id']
                # item['name'] = response.xpath(XPATH_ELEMENT['coin_fullname']).extract()[0].replace(" ","") + '-' + \
                #                response.xpath(XPATH_ELEMENT['coin_shortname']).extract()[0]

                item['name'] = response.xpath('/html/body/div[2]/div/div[1]/div[3]/div[1]/div[1]/text()').extract()[1].replace(" ", "").replace("\n", "") + '-' + \
                               response.xpath('/html/body/div[2]/div/div[1]/div[3]/div[1]/div[1]/span/text()').extract()[0]

                data = eachday_day.xpath('./td[1]/text()').extract()[0]

                if ("No data" in str(data)):
                    pass
                else:
                    datetime_struct = parser.parse(eachday_day.xpath('./td[1]/text()').extract()[0])
                    item['date'] = datetime_struct.strftime('%Y-%m-%d')
                    item['open'] = eachday_day.xpath('./td[2]/text()').extract()[0].replace("\n", "").replace(" ",
                                                                                                              "").replace(
                        ",", "").replace("-", "0")
                    item['high'] = eachday_day.xpath('./td[3]/text()').extract()[0].replace("\n", "").replace(" ",
                                                                                                              "").replace(
                        ",", "").replace("-", "0")
                    item['low'] = eachday_day.xpath('./td[4]/text()').extract()[0].replace("\n", "").replace(" ",
                                                                                                             "").replace(
                        ",", "").replace("-", "0")
                    item['close'] = eachday_day.xpath('./td[5]/text()').extract()[0].replace("\n", "").replace(" ",
                                                                                                               "").replace(
                        ",", "").replace("-", "0")
                    item['volume'] = eachday_day.xpath('./td[6]/text()').extract()[0].replace("\n", "").replace(" ",
                                                                                                                "").replace(
                        ",", "").replace("-", "0")
                    item['marketcap'] = eachday_day.xpath('./td[7]/text()').extract()[0].replace("\n", "").replace(" ",
                                                                                                                   "").replace(
                        ",", "").replace("-", "0")
                    yield item
        except:
            filepath = "/Users/ouno/Documents/Projects/Codes/Python/cryptocurrency/error_log/err.txt"
            with open(filepath, 'a+') as fp:
                traceback.print_exc(file=fp)

# def notThreadSafe(x):
#     print('not threadsafe')
#
# def crawl_run():
#     runner = CrawlerRunner()
#     runner.crawl(MainSpider)
#     d = runner.join()
#     d.addBoth(lambda _:reactor.stop())
#     reactor.callFromThread(notThreadSafe, 3)
#     reactor.run()
#
# def crawl_process():
#     process = CrawlerProcess()
#     process.crawl(MainSpider)
#     process.start()  # the script will block here until all crawling jobs are finished
#     notThreadSafe(3)


#
# execute(
#     ['scrapy', 'crawl', 'coin', "-a", "begindate=20190501", "-a", "enddate=20190503", "-a", "category=ethereum-classic",
#      "-a", "parsetype=0"])

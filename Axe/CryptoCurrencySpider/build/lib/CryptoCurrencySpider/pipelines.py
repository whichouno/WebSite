from .database import dbhandle as DBH,dbinit as DBI

class CryptocurrencyspiderPipeline(object):
    json_part = ''
    log_path = "/Users/ouno/Documents/Projects/Codes/Python/cryptocurrency/error_log/err.txt"

    def process_item(self, item, spider):
        try:
            if(spider.name == 'coin'):
                name = item['name'][:item['name'].rindex('-')].replace('-','').replace('(','').replace(')','').replace('[','').replace(']','').replace('.','').replace('/','').replace('\\','').replace('.','').replace('\'','').replace('+','')

                data = eval('DBI.Table_' + name)(date=item['date'],
                                            open=item['open'],
                                            high=item['high'],
                                            low=item['low'],
                                            close=item['close'],
                                            volume=item['volume'],
                                            marketcap = item['marketcap'])
                res = DBH.Insert(data)
                if (res[0] == False):
                    with open(self.log_path, 'ab+') as fp:
                        fp.write(str(name).encode('utf8') + str(" : ").encode('utf8') + str(res[1]).encode('utf8') + b'\n')
            else:
                pass
        except BaseException as e:
            with open(self.log_path, 'ab+') as fp:
                fp.write(str(e).encode('utf8') + b'\n')
        return item
from uuid import uuid4
from django.shortcuts import render
from .models import Bitcoin,Ethereum,Ethereumclassic,Bitcoincash,Litecoin,Eos,Neo,Bitshares
from django.core import serializers
import json,datetime
from django.http import Http404,HttpResponse
from django.db.models import Max


from uuid import uuid4
from django.http import JsonResponse
from scrapyd_api import ScrapydAPI

import threading, time

scrapyd_ip = 'localhost'
scrapyd_port = 6800
scrapyd_url = f'http://{scrapyd_ip}:{scrapyd_port}'
scrapyd = ScrapydAPI('http://localhost:6800')
print(scrapyd.list_projects())


def test(request):
    return render(request, '../templates/gallery.html')

# def schedule(project,spider):
#     url = scrapyd_url + f'/schedule.json'
#     params = {
#         "project":project,
#         "spider":spider
#     }
#     r = requests.post(url,data = params)
#     return r.json()
#
# def listjobs(project):
#     url = scrapyd_url + f'/listjobs.json?project={project}'
#     r = requests.get(url)
#     return r.json()

# command = "scrapy crawl main -a begindate='" + begindate.strftime('%Y%m%d') + "' -a enddate='" + enddate.strftime('%Y%m%d') + "' -a category='" + category + "' -a parsetype=0"
            #
            # print(command)
            # subprocess.getstatusoutput(command)
            #
            #
            # command = ['scrapy', 'crawl', 'coin',
            #          "-a", "begindate=" + begindate.strftime('%Y%m%d'),
            #          "-a", "enddate=" + enddate.strftime('%Y%m%d'),
            #          "-a", "category=" + category, "-a", "parsetype=0"]
            # print(command)
            # execute(command)

spider_dict = {}

class SpiderThread(threading.Thread):
    def __init__(self,begindate,enddate,category):
        threading.Thread.__init__(self)
        self.threadID  = None
        self.begindate = begindate
        self.enddate = enddate
        self.category = category

    def run(self):
        taskID, y = spiderCrawl(self.begindate, self.enddate, self.category)
        self.threadID = taskID
        while(True):
            job_status = scrapyd.job_status('default', taskID)
            print("job_status:", job_status)
            if(job_status == 'finished'):
                spider_dict.pop(self.category)
                break
            else:
                time.sleep(1)

def spiderCrawl(begindate,enddate,category):
        unique_id = str(uuid4())

        settings = {
            'unique_id': unique_id,  # unique ID for each record for DB
            'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        }
        taskID = scrapyd.schedule('default', 'main',
                    begindate=begindate.strftime('%Y%m%d'),
                    enddate=enddate.strftime('%Y%m%d'),
                    category=category,
                    parsetype=0)
        return taskID,JsonResponse({'task_id': taskID, 'unique_id': unique_id, 'status': 'started'})

def spiderLaunchJudge(model, category):
    max_date = model.objects.all().aggregate(Max('date'))
    begindate = max_date['date__max']
    enddate = datetime.date.today()

    print('category:', category)
    print('begindate:', begindate)
    print('enddate:', enddate)
    print('enddate - datetime.timedelta(days=1):',enddate - datetime.timedelta(days=1))

    if (begindate != enddate - datetime.timedelta(days=1)):
        # spiderCrawl(begindate, enddate, category)

        if (category in spider_dict.keys()):
            pass
        else:
            spider_dict[category] = ''
            t = SpiderThread(begindate, enddate, category)
            t.start()


def cryptocurrency(request):
    rp = request.path;
    if (not rp.endswith('/')):
        rp = rp + '/'

    category = rp.split('/')[2];
    coindataset = None

    if(category == ''):
        category = 'bitcoin'

    if(category == 'bitcoin'):
        spiderLaunchJudge(Bitcoin, category)
        coindataset = Bitcoin.objects.all()
    elif(category == 'ethereum'):
        spiderLaunchJudge(Ethereum, category)
        coindataset = Ethereum.objects.all()
    elif(category == 'ethereum-classic'):
        spiderLaunchJudge(Ethereumclassic, category)
        coindataset = Ethereumclassic.objects.all()
    elif (category == 'bitcoin-cash'):
        spiderLaunchJudge(Bitcoincash, category)
        coindataset = Bitcoincash.objects.all()
    elif(category == 'litecoin'):
        spiderLaunchJudge(Litecoin, category)
        coindataset = Litecoin.objects.all()
    elif (category == 'eos'):
        spiderLaunchJudge(Eos, category)
        coindataset = Eos.objects.all()
    elif (category == 'neo'):
        spiderLaunchJudge(Neo, category)
        coindataset = Neo.objects.all()
    elif (category == 'bitshares'):
        spiderLaunchJudge(Bitshares, category)
        coindataset = Bitshares.objects.all()
    else:
        return HttpResponse("你所访问的页面不存在",status=404)
        # return render_to_response('error_404.html', status=404)
        # return render(request, 'base_news.html')

    # datasets = Bitcoin.objects.get_queryset().filter(date='2018-05-01').values('date','open','high','low','close','volume')
    datasets = coindataset.order_by('date').values('date', 'open', 'high', 'low', 'close','volume')

    rawData = []
    for data in datasets:
        list = []
        list.append(data['date'].strftime('%Y-%m-%d'))
        list.append(data['open'])
        list.append(data['close'])
        list.append(data['low'])
        list.append(data['high'])
        list.append(data['volume'])
        rawData.append(list)

    # print(json.dumps(rawData))
    # testdata = "[[\"2018-07-14\",6247.50,6276.12,6212.22,6298.19,2923670000],[\"2018-07-03\",6596.66,6529.59,6447.75,6671.37,4672310000],[\"2018-07-01\",6411.68,6385.82,6289.29,6432.85,4788260000]]"

    return render(request, 'cryptocurrencycm/cryptocurrency.html', {'rawData': json.dumps(rawData), 'title': category})

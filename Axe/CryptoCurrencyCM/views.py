from django.shortcuts import render
from .models import Bitcoin,Ethereum,Ethereumclassic,Bitcoincash
from django.core import serializers
import json,datetime
from django.http import Http404,HttpResponse

def test(request):
    return render(request, '../templates/gallery.html')


def cryptocurrency(request):
    rp = request.path;
    if (not rp.endswith('/')):
        rp = rp + '/'

    category = rp.split('/')[2];
    coindataset = None

    if(category == ''):
        category = 'bitcoin'

    if(category == 'bitcoin'):
        coindataset = Bitcoin.objects.all()
    elif(category == 'ethereum'):
        coindataset = Ethereum.objects.all()
    elif(category == 'ethereumclassic'):
        coindataset = Ethereumclassic.objects.all()
    elif (category == 'bitcoincash'):
        coindataset = Bitcoincash.objects.all()
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

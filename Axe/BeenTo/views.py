from django.shortcuts import render,get_object_or_404
import json,datetime
from django.http import Http404,HttpResponse
from django.http import JsonResponse
from .models import ChinaProvinces,ChinaCities
from django.db.models import Count

def get_cities_by_province_name(province_name):
    rawData = []
    # citites = Cities.objects.get_queryset().filter(province__name=province_name)
    citites = ChinaCities.objects.get_queryset().filter(province__name=province_name,grade=2)
    for c in citites:
        dict = {}
        dict['name'] = c.name
        dict['value'] = [c.longitude,c.latitude]
        rawData.append(dict)
    return rawData

def set_cities_beento():
    citiesData = []
    citites = ChinaCities.objects.get_queryset().filter(grade=2,beento=1)
    for c in citites:
        dict = {}
        dict['name'] = c.name
        dict['value'] = [c.longitude, c.latitude]
        citiesData.append(dict)
    return citiesData
'''------------------------------------------------------------------------------------------------------------------------------------------
名称：
    get_cities_beento
参数：
    provinceName = ''（默认）
说明：
    查询市县的beento状态。返回市县beento状态时，使用省份作为条件查询，即只返回指定省份的市县beento状态。
    如果是在省份模式（单国家地图），传入的地区名称为国名，同''一样处理，返回所有市县beento状态。
返回：
    [],[]
    1.citiesData 市县名称及经纬度。格式：[{'name': '南京市', 'value': [118.7674, 32.0415]}, {'name': '杭州市', 'value': [120.1536, 30.2875]} ... {'name': '拉萨市', 'value': [91.1322, 29.6604]} ]
    2.provincesData 省份名称。格式：[{'name': '北京', 'selected': True}, {'name': '重庆', 'selected': True},{'name': '新疆', 'selected': True}]
------------------------------------------------------------------------------------------------------------------------------------------'''
def get_cities_beento(provinceName=''):
    citiesData = []
    provincesData = []
    citites = None
    provinces = None
    if(provinceName == '' or provinceName == 'china'):
        citites = ChinaCities.objects.get_queryset().filter(grade=2,beento=1)
        provinces = citites.values('province__name').annotate(dcount=Count('province__name'))
    else:
        citites = ChinaCities.objects.get_queryset().filter(grade=2, beento=1,province__name=provinceName)
        # annotate 效果等同于SQL group by。
        provinces = citites.values('province__name').annotate(dcount=Count('province__name'))
    for c in citites:
        dict = {}
        dict['name'] = c.name
        dict['value'] = [c.longitude, c.latitude]
        citiesData.append(dict)
    for p in provinces:
        provincesData.append({'name':p['province__name'],'selected':True})
    return citiesData,provincesData

def beento(request):
    rp = request.path;
    if(not rp.endswith('/')):
        rp = rp + '/'

    areaName = rp.split('/')[2];
    areaGrade = 0
    errMsg = 'success'
    provinceJSPath = ''

    if(areaName == ''):
        areaName = 'world'

    if (areaName == 'world'):
        areaGrade = 0
    elif (areaName == 'china'):
        if(rp.split('/')[3] != ''):
            provinceJSPath = '../../static/javascript/beento/' + areaName + '_provinces/' + rp.split('/')[3] + '.js'
            areaGrade = 2
            areaName = get_province_name_by_pinyin(rp.split('/')[3])
        else:
            areaGrade = 1
    else:
        return HttpResponse("你所访问的页面不存在", status=404)
    return render(request, 'beento/beento.html',{'areaName': areaName, 'areaGrade': areaGrade, 'provinceJSPath':provinceJSPath, 'errMsg': errMsg})

def get_province_map_path(countryName,provinceName):
    rawData = {}
    if countryName == 'china':
        provincePinYin = get_province_pinyin_by_name(provinceName)
        provinceJSPath = '../../static/javascript/beento/' + countryName + '_provinces/' + provincePinYin + '.js'
        rawData = {'pinyin':provincePinYin,'path': provinceJSPath}
    return rawData

def get_province_pinyin_by_name(provinceName):
    provincePinYin = ChinaProvinces.objects.get_queryset().filter(name=provinceName).values('pinyin')
    return provincePinYin[0]['pinyin']

def get_province_name_by_pinyin(provincePinYin):
    provinceName = ChinaProvinces.objects.get_queryset().filter(pinyin=provincePinYin).values('name')
    return provinceName[0]['name']

def ajax_get_province_pinyin(request):
    countryName = ''
    provinceName = ''
    if request.method == 'POST':
        for key in request.POST:
            countryName = eval(key)["countryName"]
            provinceName = eval(key)["provinceName"]

    rawData = { 'pinyin':get_province_pinyin_by_name(provinceName) }
    return JsonResponse(rawData, safe=False)

'''------------------------------------------------------------------------------------------------------------------------------------------
名称：
    ajax_get_cities_beento
参数：
    request
    格式：<QueryDict: {'{"areaName":"china"}': ['']}>
说明：
    js调用。查询市县的beento状态。在echart_init()中调用，即进入省、市县地图模式时，都会调用。返回市县beento状态时，使用省份作为条件查询，即只返回指定省份的市县beento状态。
    如果是在省份模式（单国家地图），传入的地区名称为国名，同''一样处理，返回所有市县beento状态。
返回：
    <JsonResponse status_code=200, "application/json">
    格式：{
            'citiesData': [ 
                {'name': '朝阳区', 'value': [116.4855, 39.9484]},  
                {'name': '海淀区', 'value': [116.2981, 39.9593]}, 
                {'name': '西安市', 'value': [108.948, 34.2632]},
                {'name': '阿勒泰地区', 'value': [88.1396, 47.8484]}
            ], 
            'regions': [
                {'name': '朝阳区', 'selected': True}, 
                {'name': '海淀区', 'selected': True}, 
                {'name': '西安市', 'selected': True}, 
                {'name': '阿勒泰地区', 'selected': True}, 
                {'name': '北京', 'selected': True},
                {'name': '陕西', 'selected': True}, 
                {'name': '新疆', 'selected': True}
            ]
        }
------------------------------------------------------------------------------------------------------------------------------------------'''
def ajax_get_cities_beento(request):
    # print(request.POST.keys['areaName'])
    areaName = ''
    if request.method == 'POST':
        for key in request.POST:
            areaName = eval(key)["areaName"]

    citiesData,provincesData = get_cities_beento(areaName)

    regions = []
    for cd in citiesData:
        regions.append({'name':cd['name'],'selected':True})

    regions = regions + provincesData
    rawData = { 'citiesData': citiesData, 'regions':regions }
    return JsonResponse(rawData, safe=False)

'''------------------------------------------------------------------------------------------------------------------------------------------
名称：
    ajax_update_cities_beento_status
参数：
    request
说明：
    js调用。市县点选时更新市县的beento状态。返回更新后的市县beento状态时，使用省份作为条件查询，即只返回指定省份的市县beento状态。
返回：
    <JsonResponse status_code=200, "application/json">
    格式：{
            'citiesData': [ 
                {'name': '朝阳区', 'value': [116.4855, 39.9484]},  
                {'name': '海淀区', 'value': [116.2981, 39.9593]}, 
                {'name': '西安市', 'value': [108.948, 34.2632]},
                {'name': '阿勒泰地区', 'value': [88.1396, 47.8484]}
            ], 
            'regions': [
                {'name': '朝阳区', 'selected': True}, 
                {'name': '海淀区', 'selected': True}, 
                {'name': '西安市', 'selected': True}, 
                {'name': '阿勒泰地区', 'selected': True}, 
                {'name': '北京', 'selected': True},
                {'name': '陕西', 'selected': True}, 
                {'name': '新疆', 'selected': True}
            ]
        }
------------------------------------------------------------------------------------------------------------------------------------------'''
def ajax_update_cities_beento_status(request):
    print(request.POST)
    provinceName = ''
    cityName = ''
    if request.method == 'POST':
        for key in request.POST:
            provinceName = eval(key)["provinceName"]
            cityName = eval(key)["cityName"]

    res = ChinaCities.objects.get_queryset().filter(province__name=provinceName, name=cityName, grade=2)
    if(res.values('beento') != None and res.values('beento').count() > 0):
        hasbeento = res.values('beento')[0]['beento']
        if(hasbeento == 0):
            res.update(beento=1)
        else:
            res.update(beento=0)

        citiesData,provincesData = get_cities_beento(provinceName)

        regions = []
        for cd in citiesData:
            regions.append({'name': cd['name'], 'selected': True})

        regions = regions + provincesData

        rawData = {'citiesBeenToData': citiesData,'regions':regions}
        return JsonResponse(rawData, safe=False)
    else:
        print("error !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")






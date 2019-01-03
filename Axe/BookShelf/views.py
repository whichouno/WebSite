from django.shortcuts import render,get_object_or_404
from .models import Books,States,Authors,Continents,BookStatus
from django.core import serializers
import json,datetime
from django.http import Http404,HttpResponse
from django.http import JsonResponse
from django.contrib import auth
from django.db.models import Count

label_setting = {
    'color':'#000000',
    'fontSize': 13,
    'fontWeight': 500,
    'position':'inside',
    'borderWidth':0,
    'verticalAlign':'middle',
    'align':'center',
    'formatter': '{b}'
}

continent_names_en_to_cn = {'asian':'亚洲','europe':'欧洲','northamerica':'北美洲','southamerica':'南美洲','africa':'非洲','oceania':'大洋洲'}

def datahandle(tree,book):
    leaves_itemStyle_setting = {
        'color': book.status.color,
        'borderWidth': 0,
        'borderType': 'solid',
        'borderColor': '#179990',
        'label': label_setting
    }
    # fontStyle: 'italic',
    # fontWeight: 900,
    # fontSize: 20,

    state_index = -1
    has_state = False
    for state_key in tree['children']:
        state_index = state_index + 1
        if (book.author.state.name == state_key['name']):
            has_state = True
            break
        else:
            pass

    author_index = -1
    has_author = False
    if(has_state):
        for author_key in tree['children'][state_index]['children']:
            author_index = author_index + 1
            if(book.author.name == author_key['name']):
                has_author = True
                break
            else:
                pass

        book_index = -1
        has_book = False
        if(has_author):
            for book_key in tree['children'][state_index]['children'][author_index]['children']:
                book_index = book_index + 1
                if(book.name == book_key['name']):
                    has_book = True
                    break
                else:
                    pass

            if(has_book):
                pass
            else:
                # print('无该书籍分支,新增书籍分支')
                tree['children'][state_index]['children'][author_index]['children'].append(
                    {'name': "《" + book.name + "》", 'status': book.status.description, 'symbol': 'rect','symbolSize': [200,20], 'label':label_setting, 'itemStyle':leaves_itemStyle_setting, 'id':book.id})
        else:
            # print('无该作者分支,新增作者分支')
            tree['children'][state_index]['children'].append(
                {'name': book.author.name, 'children': [{'name': "《" + book.name + "》", 'status': book.status.description, 'symbol': 'rect','symbolSize': [200,20], 'label':label_setting, 'itemStyle':leaves_itemStyle_setting, 'id':book.id}]})
    else:
        # print('无该国家分支,新增国家分支')
        tree['children'].append({'name': book.author.state.name, 'children': [
            {'name': book.author.name, 'children': [{'name': "《" + book.name + "》", 'status': book.status.description, 'symbol': 'rect','symbolSize': [200,20], 'label':label_setting, 'itemStyle':leaves_itemStyle_setting, 'id':book.id}]}]})
    return tree

def get_read_count():
    dict = {}
    res = Books.objects.get_queryset().values('status_id').annotate(dcount=Count('status_id'))
    for r in res:
        if(r['status_id'] == 1):
            dict['unread_count'] = r['dcount']
        elif(r['status_id'] == 2):
            dict['reading_count'] = r['dcount']
        elif(r['status_id'] == 3):
            dict['read_count'] = r['dcount']
    return dict

def bookshelf(request):
    rp = request.path;
    if (not rp.endswith('/')):
        rp = rp + '/'

    category = rp.split('/')[2];

    if (category == ''):
        category = 'all'

    errMsg = 'success'
    if request.method == "POST":
        name = request.POST.get("name", None)
        birth = request.POST.get("birth", None)
        death = request.POST.get("death", None)
        abstract = request.POST.get("abstract", None)
        book = request.POST.get("book", None)
        continent = request.POST.get("continent", None)
        state = request.POST.get("state",None)

        try:
            has_author = Authors.objects.get_queryset().filter(name=name,birth = birth,death = death)
            if(has_author.__len__() <= 0):
                Authors.objects.create(
                    name = name,
                    birth = birth,
                    death = death,
                    abstract = abstract,
                    state_id = state
                )
                has_author = Authors.objects.get_queryset().filter(name=name, birth=birth, death=death)

            author_id = has_author[0].id
            # bookshelf.books(name, author_id)
            Books.objects.create(
                name = book,
                author_id = author_id
            )
        except Exception as ex:
            errMsg = ex

    books_data_list = []
    continents_list = None

    if('all' == category):
        continents_list = Continents.objects.all()
    else:
        continents_list = Continents.objects.all().filter(name=continent_names_en_to_cn[category])

    for continent in continents_list:
        tree = {'name': continent.name, 'children': [{'name': '', 'children': [{'name': '', 'children': [{'name': '', 'status': 1, 'count': 1}]}]}]}
        books_data = Books.objects.get_queryset().filter(author__state__continent_id=continent.id)

        rawData = {}
        if(books_data.__len__() > 0):
            for book in books_data:
                rawData = datahandle(tree,book)
            rawData['children'].pop(0)
            books_data_list.append(rawData)

    if ('all' == category):
        data = {'name': '阅读列表', 'children': books_data_list}
    else:
        if(books_data_list.__len__() > 0):
            data = books_data_list[0]
        else:
            data = {'name': '无', 'children': books_data_list}

    res = get_read_count()
    unread_count = res['unread_count']
    reading_count = res['reading_count']
    read_count = res['read_count']
    read_all_count = unread_count + reading_count + read_count
    response = render(request, 'bookshelf/bookshelf.html', {'rawData': json.dumps(data), 'unread_count':unread_count, 'reading_count':reading_count, 'read_count':read_count, 'read_all_count':read_all_count, 'err_msg':errMsg, 'title':category})
    # response.setdefault('Cache-Control','no-store')
    # response.setdefault('Expires',0)
    # response.setdefault('Program','no-cache')
    return response

def ajax_continent(request):
    continents_list = Continents.objects.get_queryset().values('id','name')

    rawData = []
    for continent in continents_list:
        rawData.append(continent)

    return JsonResponse(rawData, safe=False)

# @csrf_exempt
def ajax_state(request):
    if request.method == "POST":
        for key in request.POST:
            continent_id = int(eval(key)["continent_id"])

    states_list = States.objects.get_queryset().filter(continent__id=continent_id).values('id','name')

    rawData = []
    for state in states_list:
        rawData.append(state)

    return JsonResponse(rawData, safe=False)

def ajax_update_book_status(request):
    if request.method == "POST":
        for key in request.POST:
            book_id = int(eval(key)["bookID"])

    res = Books.objects.get_queryset().filter(id=book_id)

    status_id = res.values('status_id')[0]['status_id']
    if(status_id == 1):
        res.update(status_id=2)
    elif(status_id == 2):
        res.update(status_id=3)
    elif(status_id == 3):
        res.update(status_id=1)

    res = Books.objects.get_queryset().filter(id=book_id)

    rawData = {'status_id': res.values('status_id')[0]['status_id'],'description': res.values('status__description')[0]['status__description'], 'color': res.values('status__color')[0]['status__color']}
    return JsonResponse(rawData, safe=False)

def ajax_get_read_count(request):
    rawData = get_read_count()
    return JsonResponse(rawData, safe=False)

def ajax(request):
    print("ajax:",request.path)
    pass
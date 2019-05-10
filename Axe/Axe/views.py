from django.shortcuts import render

# def index(request):
#     print("Axe.views.index")
#     return render(request, 'index.html')

def index(request):
    print("Axe.views.index")
    return render(request, 'index.html')

import json
from django.http import JsonResponse
# def test(request):
#     with open("/Users/ouno/Project/WebSite/Axe/static/mock.json", 'r') as load_f:
#         load_dict = json.load(load_f)
#         print(type(load_dict))
#         data = json.dumps(load_dict)
#     return JsonResponse(data,safe=False)

import socket
def test(request):
    with open("/Users/ouno/Project/WebSite/Axe/static/mock.json", 'r') as load_f:
        load_dict = json.load(load_f)
        print(type(load_dict))
        data = json.dumps(load_dict)

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = ("0.0.0.0",8765)
    sock.bind(host)
    sock.listen(5)
    print("ws server running")
    while(True):
        print("waiting...")
        connect,address = sock.accept()
        print("accept connect")
        message = connect.recv(2048)
        print("recv data:",message)
        connect.send(data.encode())
        print("send data:",data)
        connect.close()

def page_not_found(request):
    return render(request, '404.html')


def page_error(request):
    return render(request, '../templates/500.html')


def permission_denied(request):
    return render(request, '../templates/403.html')

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error
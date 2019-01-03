from django.shortcuts import render

# def index(request):
#     print("Axe.views.index")
#     return render(request, 'index.html')

def index(request):
    print("Axe.views.index")
    return render(request, 'index.html')

def page_not_found(request):
    return render(request, '404.html')


def page_error(request):
    return render(request, '../templates/500.html')


def permission_denied(request):
    return render(request, '../templates/403.html')

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error
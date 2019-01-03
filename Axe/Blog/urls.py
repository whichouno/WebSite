from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.cryptocurrency),
]


# urlpatterns = [
#     path(r'^(?P<year>\d{4})$', views.chart(),name='chart'),
# ]
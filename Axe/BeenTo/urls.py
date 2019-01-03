from . import regex, views
from django.urls import register_converter, path, re_path

register_converter(regex.FourDigitYearConverter, 'yyyy')
# path('articles/<yyyy:year>/', views.year_archive),

urlpatterns = [
    path('', views.beento),
    path('world/', views.beento),
    path('china/', views.beento),
    re_path('china/*', views.beento),

    path('ajax_get_province_pinyin',views.ajax_get_province_pinyin),
    path('ajax_update_cities_beento_status',views.ajax_update_cities_beento_status),
    path('ajax_get_cities_beento',views.ajax_get_cities_beento),

]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.cryptocurrency),
    path('bitcoin/', views.cryptocurrency),
    path('ethereum/', views.cryptocurrency),
    path('ethereum-classic/', views.cryptocurrency),
    path('bitcoin-cash/', views.cryptocurrency),
    path('litecoin/', views.cryptocurrency),
    path('eos/', views.cryptocurrency),
    path('neo/', views.cryptocurrency),
    path('bitshares/', views.cryptocurrency),
]
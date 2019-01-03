from . import views
from django.urls import path

urlpatterns = [
    path('', views.cryptocurrency),
    path('bitcoin/', views.cryptocurrency),
    path('ethereum/', views.cryptocurrency),
    path('ethereumclassic/', views.cryptocurrency),
    path('bitcoincash/', views.cryptocurrency),
]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.bookshelf),
    path('all', views.bookshelf),
    path('asian', views.bookshelf),
    path('europe', views.bookshelf),
    path('northamerica', views.bookshelf),
    path('southamerica', views.bookshelf),
    path('africa', views.bookshelf),
    path('oceania', views.bookshelf),

    path('ajax_continent',views.ajax_continent),
    path('ajax_state',views.ajax_state),
    path('ajax_update_book_status',views.ajax_update_book_status),
    path('ajax_get_read_count',views.ajax_get_read_count),
]
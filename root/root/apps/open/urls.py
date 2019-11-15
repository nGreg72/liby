from django.urls import path

from . import views

urlpatterns = [
    path('', views.Zakup_list, name='index'),
    path('<str:id>/', views.zakup_detail, name='zakup_id_url'),
    path('open/<id>/', views.row_detail, name='row_id_url')
]

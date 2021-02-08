from django.urls import path
from . import views

app_name = 'wisely'

urlpatterns = [
    path('', views.index_view, name='index_url'),
    path('morning/', views.morning_view, name='morning_url'),
    path('morning_ajax/', views.morning_ajax, name='morning_ajax_url'),
    path('morning_del_ajax/', views.morn_del_ajax, name='morning_del_ajax_url'),
    path('evening/', views.evening_view, name='evening_url'),
    path('evening_ajax/', views.evening_ajax, name='evening_ajax_url'),
    path('even_del_ajax/', views.even_del_ajax, name='even_del_ajax_url'),
    path('morn_redirect/', views.morn_redirect, name='morn_redirect_url'),
    path('anchor/', views.anchor_view, name='anchor_url'),
    path('anchor_del', views.anchor_del_view, name='anchor_del_url'),
    path('anchor_update', views.anchor_update_view, name='anchor_update_url')
]
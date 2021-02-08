from django.urls import path
from . import views
app_name = 'registration'

urlpatterns = [
    path('signup/', views.signup_view, name='signup_url'),
    path('login/', views.login_view, name='login_url'),
    path('logout/', views.logout_view, name='logout_url'),
    path('user_exist_check/', views.user_exist_check, name='user_exist_check_url'),
    path('authentication_check/', views.authentication_check, name='authentication_check'),
]
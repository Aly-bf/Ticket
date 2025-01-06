from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.Home.as_view(),name='home'),
    path('login_user', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
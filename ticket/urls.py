from . import views
from django.urls import path

app_name = 'ticket'
urlpatterns = [
    path('', views.ticket, name='ticket'),
    path('ticket_list', views.ticket_list, name='ticket_list'),
    path('delete/<int:pk>/', views.delete_ticket, name='delete'),
    path('detail/<int:pk>/', views.ticket_detail, name='detail')
]
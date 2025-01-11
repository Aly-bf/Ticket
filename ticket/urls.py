from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TicketList)



app_name = 'ticket'
urlpatterns = [
    path('', views.ticket, name='ticket'),
    path('ticket_list', views.ticket_list, name='ticket_list'),
    path('delete/<int:pk>/', views.delete_ticket, name='delete'),
    path('detail/<int:pk>/', views.ticket_detail, name='detail'),
    path('viewsets/', include(router.urls)),

]
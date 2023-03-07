from django.urls import path
from base.views import order_views as views

urlpatterns = [
    path('', views.getOrders, name='orders'),
    path('add/', views.addOrderItems, name='orders_add'),
    path('myorders/', views.getMyOrders, name='my_orders'),
    path('<str:pk>/deliver/', views.updateOrderToDelivered, name='user_delivered'),
    path('<str:pk>/', views.getOrderById, name='user_order'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
]
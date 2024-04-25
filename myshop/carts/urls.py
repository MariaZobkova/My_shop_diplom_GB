
from django.urls import path
from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart_remove/<int:cart_id>', views.cart_remove, name='cart_remove'),
]
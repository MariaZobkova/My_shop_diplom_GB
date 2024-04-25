
from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('<int:category_id>/', views.catalog, name="index"),
    path('<int:category_id>/<int:page>/', views.catalog, name="index"),
    path('product/<int:product_id>/', views.product, name="product")
]
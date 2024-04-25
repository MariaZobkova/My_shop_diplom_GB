from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('info/', views.info, name="info")
]
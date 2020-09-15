from django.urls import path
from . import views

urlpatterns = [
    path('geocoder/', views.view_map, name='map'),
    path('', views.view_map, name='maps')

]
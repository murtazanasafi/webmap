from django.urls import path
from . import views

urlpatterns = [
    path('geocoder/', views.view_map, name='map'),
    path('', views.homepage, name='home'),
    path('esri', views.pasap_map, name='pasap'),

]
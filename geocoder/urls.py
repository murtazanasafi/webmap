from django.urls import path
from . import views

urlpatterns = [
    path('geocoder/', views.view_map, name='map'),
    path('home/', views.homepage, name='home'),
    # path('psap/', views.pasap_map, name='pasap'),
    path('', views.homepage, name='home')

]
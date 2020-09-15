from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

def redirect_view(request):
    response = redirect('/geocoder')
    return response

def view_map(request):
    return render(request, template_name='geocoder.html')

def pasap_map(request):
    return render(request, template_name='pasap.html')

def homepage(request):
    return render(request, template_name='homepage.html')
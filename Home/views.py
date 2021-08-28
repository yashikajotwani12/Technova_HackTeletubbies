from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'Home/home.html')

class home(ListView):
    template_name='Home/home.html'

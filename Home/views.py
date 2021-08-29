from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'Home/home.html')
def news(request):
    return render(request,'Home/news.html')
def cryptobot(request):
    return render(request,'Home/cryptobot.html')

class home(ListView):
    template_name='Home/home.html'

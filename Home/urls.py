from django.urls import path
from Home import views
app_name = 'Home'


urlpatterns =[
    path('',views.index,name='home'),
    path('news',views.news,name="news"),
    path('cryptobot',views.cryptobot,name="cryptobot")
]
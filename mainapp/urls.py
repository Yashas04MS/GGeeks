from django.urls import path, include
from django.contrib import admin
from .views import home,getdata,about
# from home import views
app_name='mainapp'

urlpatterns = [
    path('',home,name='home'),
    path('about/', about, name='about'),

    path('getdata/<str:input>',getdata,name='getdata'),

]

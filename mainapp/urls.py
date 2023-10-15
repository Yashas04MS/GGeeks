from django.urls import path, include
from .views import home,getdata
app_name='mainapp'

urlpatterns = [
    path('',home,name='home'),
    path('getdata/<str:input>',getdata,name='getdata'),
]

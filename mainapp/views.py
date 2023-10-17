from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .translator import translator
def getdata(request,input):
    result=translator(input)
    print(result)
    return JsonResponse({'data':result})
def home(request):
    return render(request,'mainapp/home.html')



# adding files here from cpy

def about(request):
    return render(request,'mainapp/about.html')
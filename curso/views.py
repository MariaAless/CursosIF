from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Curso_info,Curso_Ali,Curso_Api


def index(request):
    return render(request, 'code/index.html')

def info(request):
    info= Curso_info.objects.all()
    context = {'info' : info}
    return render(request,'code/informatica.html',context)

def ali(request):
    ali= Curso_Ali.objects.all()
    context={'alimentos': ali}
    return render(request,'code/alimentos.html',context)

def api(request):
    api= Curso_Api.objects.all()
    context={'apicultura': api}
    return render(request,'code/apicultura.html',context)


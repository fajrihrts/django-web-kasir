from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_name = 'index.html'
    contex = {
        'title': 'Kasir',
    }   
    return render(request, template_name, contex)

def about(request):
    template_name = 'about.html'
    contex = {
        'title': 'About',
    }   
    return render(request, template_name, contex)

def barang(request):
    template_name = 'barang.html'
    contex = {
        'title': 'barang',
    }   
    return render(request, template_name, contex)

def order(request):
    template_name = 'order.html'
    contex = {
        'title': 'order',
    }   
    return render(request, template_name, contex)
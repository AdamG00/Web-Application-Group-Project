from django.shortcuts import render
from django.http import HttpResponse
from . models import Page

def index(request):
    pg = Page.objects.get(permalink='/')
    context = {
	'title': pg.title,
	'content': pg.bodytext
    }
    return render(request, 'base.html', context)

def about(request):
    pg = Page.objects.get(permalink='/about')
    context = {
	'title': pg.title,
	'content': pg.bodytext
    }
    return render(request, 'base.html', context)

def login(request):
    pg = Page.objects.get(permalink='/login')
    context = {
	'title': pg.title,
	'content': pg.bodytext
    }
    return render(request, 'base.html', context)

def signup(request):
    pg = Page.objects.get(permalink='/signup')
    context = {
	'title': pg.title,
	'content': pg.bodytext
    }
    return render(request, 'base.html', context)

def magic(request):
    pg = Page.objects.get(permalink='/magic')
    context = {
	'title': pg.title,
	'content': pg.bodytext
    }
    return render(request, 'base.html', context)

# Create your views here.

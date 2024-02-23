from django.shortcuts import render
from django.http import HttpResponse
from . models import Page

def index(request):
    pg = Page.objects.get(permalink='/')
    return HttpResponse(pg.bodytext)

def about(request):
    pg = Page.objects.get(permalink='/')
    return HttpResponse(pg.bodytext)

def login(request):
    pg = Page.objects.get(permalink='/')
    return HttpResponse(pg.bodytext)

def signup(request):
    pg = Page.objects.get(permalink='/')
    return HttpResponse(pg.bodytext)

def magic(request):
    pg = Page.objects.get(permalink='/')
    return HttpResponse(pg.bodytext)

# Create your views here.

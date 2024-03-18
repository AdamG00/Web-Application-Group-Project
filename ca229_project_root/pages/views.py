from django.shortcuts import render
from django.http import HttpResponse
from . models import Page

def index(request):
    pg = Page.objects.get(permalink='/')
    context = {
		'title': pg.title,
		'content': pg.bodytext,
        'daily': pg.daily_challenge,
		'last_updated': pg.update_date,
		'page_list': Page.objects.all(),
	}
    return render(request, 'pages/indexpage.html', context)

def about(request):
    pg = Page.objects.get(permalink='/about')
    context = {
		'title': pg.title,
		'content': pg.bodytext,
		'last_updated': pg.update_date,
		'page_list': Page.objects.all(),
	}
    return render(request, 'pages/aboutpage.html', context)

def login(request):
    pg = Page.objects.get(permalink='/login')
    context = {
		'title': pg.title,
		'content': pg.bodytext,
		'last_updated': pg.update_date,
		'page_list': Page.objects.all(),
	}
    return render(request, 'pages/loginpage.html', context)

def signup(request):
    pg = Page.objects.get(permalink='/signup')
    context = {
		'title': pg.title,
		'content': pg.bodytext,
		'last_updated': pg.update_date,
		'page_list': Page.objects.all(),
	}
    return render(request, 'pages/signuppage.html', context)

def magic(request):
    pg = Page.objects.get(permalink='/magic')
    context = {
		'title': pg.title,
		'content': pg.bodytext,
		'last_updated': pg.update_date,
		'page_list': Page.objects.all(),
	}
    return render(request, 'pages/magicpage.html', context)
def magic_page(request, num1, op, num2, op2, num3):
    result = 0
    if op == '+' and op2 == '+':
        result = num1 + num2 + num3
    elif op == '-' and op2 == '-':
        result = num1 - num2 - num3
    return render(request, 'magic.html', {'result': result})

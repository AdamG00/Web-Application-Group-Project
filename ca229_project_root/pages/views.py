from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

from . models import Page
from .contact import ContactForm

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

def contact(request):
	submitted = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@dcu.ie'),
				['student@dcu.ie'], # change this
				connection=con
			)
			return HttpResponseRedirect('/contact?submitted=True')
	else:
		form = ContactForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form': form,
		'page_list': Page.objects.all(),
		'submitted': submitted
	}
	return render(request, 'pages/contactpage.html', context)

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

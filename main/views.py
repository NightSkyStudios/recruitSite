from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Work

from django.utils.translation import check_for_language


# Create your views here.


def index(request):
    ctx = {'index': True}

    return render(request, 'index.html', ctx)


def about(request):
    ctx = {'about': True}

    return render(request, 'about.html', ctx)


def send_email(request):
    fname = request.POST.get('fname', '')
    lname = request.POST.get('lname', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    messages = 'Name: {}\n  Surname: {}\n{} \n\nFrom {}'.format(fname, lname, message, from_email)
    send_mail(subject, messages, 'nightskystudiosofficial@gmail.com', ['thesever99@gmail.com'],
              fail_silently=False)

    return HttpResponseRedirect('/contact/')


def contact(request):
    ctx = {'contact': True}

    if request.method == 'POST':
        send_email(request)

    return render(request, 'contact.html', ctx)


def work(request):
    works = Work.objects.all()

    ctx = {
        'work': True,
        'works': works
    }

    return render(request, 'work.html', ctx)


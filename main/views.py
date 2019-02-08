from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Work


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
    message = '{} {} /n {}'.format(fname, lname, message)
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, 'nightsktstudiosofficial@gmail.com', ['oles.hobor@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')


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

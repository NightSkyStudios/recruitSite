from django.shortcuts import render
from main.models import Work


# Create your views here.


def index(request):
    ctx = {'index': True}

    return render(request, 'index.html', ctx)


def about(request):
    ctx = {'about': True}

    return render(request, 'about.html', ctx)


def contact(request):
    ctx = {'contact': True}

    return render(request, 'contact.html', ctx)




def work(request):
    works = Work.objects.all()

    ctx = {
        'work': True,
        'works': works
    }

    return render(request, 'work.html', ctx)

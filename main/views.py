from django.shortcuts import render


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


def services(request):
    ctx = {'services': True}

    return render(request, 'services.html', ctx)


def work(request):
    ctx = {'work': True}

    return render(request, 'work.html', ctx)

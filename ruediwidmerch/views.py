from django.shortcuts import render

from .illustration.models import Illustration
from .illustration.models import Category
from .grafik.models import Grafik
from .grafik.models import Categoryg
from .news.models import News
from .portrait.models import Portrait


def home(request):
    cartoons = Illustration.objects.order_by('ordering')
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'cartoons': cartoons,
        'categories': categories,
    })


def grafik(request):
    cartoons = Grafik.objects.order_by('ordering')
    categories = Categoryg.objects.all()

    return render(request, 'grafik.html', {
        'cartoons': cartoons,
        'categories': categories,
    })


def news(request):
    newss = News.objects.all()

    return render(request, 'aktuell.html', {
        'newss': newss,
    })


def newsyear(request, year):
    newsall = News.objects.all()
    newss = News.objects.filter(date__year=year)

    return render(request, 'aktuell.html', {
        'currentyear': year,
        'newsall': newsall,
        'newss': newss,
    })


def portrait(request):
    portraits = Portrait.objects.all()

    return render(request, 'portrait.html', {
        'portraits': portraits,
    })


def contact(request):
    return render(request, 'contact.html', {
    })

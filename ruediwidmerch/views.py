from django.shortcuts import render

from .cartoons.models import Cartoon
from .cartoons.models import Category
from .column.models import Column
from .events.models import Event
from .news.models import News
from .portrait.models import Portrait


def home(request):
    cartoons = Cartoon.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'cartoons': cartoons,
        'categories': categories,
    })


def column(request):
    columns = Column.objects.all()

    return render(request, 'texte.html', {
        'columns': columns,
    })


def news(request):
    newss = News.objects.all()
    events = Event.objects.all()

    return render(request, 'news.html', {
        'newss': newss,
        'events': events,
    })


def portrait(request):
    portraits = Portrait.objects.all()

    return render(request, 'portrait.html', {
        'portraits': portraits,
    })


def contact(request):
    return render(request, 'contact.html', {
    })

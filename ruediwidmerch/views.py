from django.shortcuts import render

from .illustration.models import Illustration
from .illustration.models import Category
from .grafik.models import Grafik
from .grafik.models import Categoryg
from .news.models import News
from .portrait.models import Portrait


def home(request):
    cartoons = list(Illustration.objects.order_by('ordering'))
    categories = Category.objects.all()
    cat_x_car = len(cartoons) / categories.count()

    for i in range(0, categories.count()):
        cartoons.insert((i+1)*cat_x_car, categories[i])

    print cartoons

    return render(request, 'index.html', {
        'cartoons': cartoons,
        'categories': categories,
    })


def illustration_detail(request, id):
    cartoon = Illustration.objects.get(id=id)

    if request.is_ajax():
        return render(request, 'illustration_detail_ajax.html', {'cartoon': cartoon})
    else:
        return render(request, 'illustration_detail.html', {'cartoon': cartoon})


def grafik(request):
    cartoons = list(Grafik.objects.order_by('ordering'))
    categories = Categoryg.objects.all()
    cat_x_car = len(cartoons) / categories.count()

    for i in range(0, categories.count()):
        cartoons.insert((i+1)*cat_x_car, categories[i])

    print cartoons

    return render(request, 'grafik.html', {
        'cartoons': cartoons,
        'categories': categories,
    })


def grafik_detail(request, id):
    cartoon = Grafik.objects.get(id=id)

    if request.is_ajax():
        return render(request, 'grafik_detail_ajax.html', {'cartoon': cartoon})
    else:
        return render(request, 'grafik_detail.html', {'cartoon': cartoon})


def news(request):
    newss = News.objects.all()

    return render(request, 'aktuell.html', {
        'newss': newss,
        'newsall': newss,
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

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from virginityapp import models


def index(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')


def phone_request(request):
    if request.method == 'POST':
        return HttpResponse("Okay.")
    else:
        return render(request, 'phone.html')


def menu(request):
    context = {'dishes': []}
    for i in models.Dish.objects.all():
        picture = models.DishImage.objects.filter(to=i)
        tmp = {'picture': picture[0] if picture else None, 'value': i}
        context['dishes'].append(tmp)
    return render(request, 'menu.html', context)
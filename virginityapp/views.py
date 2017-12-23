from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from virginityapp import models


def index(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')

#@login_required(login_url='/login/')
def menu(request):
    context = {'dishes': []}
    for i in models.Dish.objects.all():
        picture = models.DishImage.objects.filter(to=i)
        tmp = {'picture': picture[0] if picture else None, 'value': i}
        context['dishes'].append(tmp)
    return render(request, 'menu.html', context)


def dish(request, dish_id):
    try:
        current_dish = models.Dish.objects.get(id=dish_id)
        picture = models.DishImage.objects.filter(to=current_dish)
        context = {'picture': picture[0] if picture else None, 'value': current_dish}
        return render(request, 'dish.html', context)
    except Exception:
        return HttpResponse(404)


def add_to_cart(request, dish_id):
    dish = models.Dish.objects.get(id=dish_id)
    if request.method == 'POST':
        item = models.Cart(user=request.user, dish=dish)
        item.save()
        return HttpResponse('OK')


@login_required
def phone_request(request):
    if request.method == 'POST':
        return HttpResponse("Okay.")
    else:
        return render(request, 'phone.html')


@login_required
def order(request, order_id):
    order = models.Order.objects.get(id=order_id, client=request.user.id)
    if order is not None:
        context = {'order': order,
                   'items': []}
        order_items = models.OrderItem.objects.filter(order=order)
        for item in order_items:
            context['items'].append(item)
        return render(request, 'order.html', context)

def basket(request):
    cart = models.Cart.objects.all()#filter(user=request.user)
    context = {'items': []}
    for i in cart:
        picture = models.DishImage.objects.filter(to=i.dish)
        i.dish.picture = picture[0]
        print(i.dish.picture)
        context['items'].append(i)
    return render(request, 'basket.html', context)
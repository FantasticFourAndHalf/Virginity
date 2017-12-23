from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from virginityapp import models


def index(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')


@login_required(login_url='/login/')
def menu(request):
    context = {'dishes': []}
    for i in models.Dish.objects.all():
        picture = models.DishImage.objects.filter(to=i)
        tmp = {'picture': picture[0] if picture else None, 'value': i}
        context['dishes'].append(tmp)
    return render(request, 'menu.html', context)


@login_required(login_url='/login/')
def dish(request, dish_id):
    try:
        current_dish = models.Dish.objects.get(id=dish_id)
        picture = models.DishImage.objects.filter(to=current_dish)
        context = {'picture': picture[0] if picture else None, 'value': current_dish}
        return render(request, 'dish.html', context)
    except Exception:
        return HttpResponse(404)


@login_required(login_url='/login/')
def add_to_cart(request, dish_id):
    dish = models.Dish.objects.get(id=dish_id)
    try:
        item = models.Cart.objects.get(dish=dish_id, user=request.user)
        item.multiplicity += 1
    except models.Cart.DoesNotExist:
        item = models.Cart(user=request.user, dish=dish)
    item.save()
    return HttpResponse('OK')


@login_required(login_url='/login/')
def delete_from_cart(request, item_id):
    cart = models.Cart.objects.get(id=item_id, user=request.user)
    cart.delete()
    return HttpResponse('OK')


@login_required(login_url='/login/')
def change_cart_amount(request, item_id, amount):
    cart = models.Cart.objects.get(id=item_id, user=request.user)
    cart.multiplicity = amount
    cart.save()
    return HttpResponse('OK')


@login_required(login_url='/login/')
def order(request, order_id):
    order = models.Order.objects.get(id=order_id, client=request.user.id)
    if order is not None:
        context = {'order': order,
                   'items': []}
        order_items = models.OrderItem.objects.filter(order=order)
        for i in order_items:
            picture = models.DishImage.objects.filter(to=i.dish)
            i.dish.picture = picture[0]
            context['items'].append(i)
        return render(request, 'order.html', context)
    else:
        return menu(request)


@login_required(login_url='/login/')
def make_order(request):
    cart = models.Cart.objects.filter(user=request.user)
    if len(cart) > 0:
        new_order = models.Order(client=request.user)
        new_order.save()
        for i in models.Cart.objects.filter(user=request.user):
            item = models.OrderItem(order=new_order, dish=i.dish, multiplicity=i.multiplicity)
            item.save()
            i.delete()
        return order(request, new_order.id)
    else:
        return menu(request)


@login_required(login_url='/login/')
def phone_request(request):
    if request.method == 'POST':
        return HttpResponse("Okay.")
    else:
        return render(request, 'phone.html')


@login_required(login_url='/login/')
def basket(request):
    cart = models.Cart.objects.filter(user=request.user)
    context = {'items': []}
    for i in cart:
        picture = models.DishImage.objects.filter(to=i.dish)
        i.dish.picture = picture[0]
        context['items'].append(i)
    return render(request, 'basket.html', context)


@login_required(login_url='/login/')
def user(request):
    orders = models.Order.objects.filter(client=request.user)
    context = {'orders': order}
    return render(request, 'user.html', context)

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class User(AbstractUser):
    phone = models.CharField(max_length=12, blank=False)
    address = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Address(models.Model):
    client = models.ForeignKey(User, related_name='address_client')
    name = models.CharField(max_length=64, blank=True)
    value = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.name + "(" + self.value + ")"


class Product(models.Model):
    name = models.CharField(max_length=64, blank=False)
    amount = models.FloatField(default=0, blank=False)
    price = models.DecimalField(blank=False, default=1, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name + "[" + str(self.amount) + "]"


class Dish(models.Model):
    name = models.CharField(max_length=128, blank=False)
    time = models.FloatField(blank=False, default=0)
    proteins = models.FloatField(blank=False, default=0)
    fats = models.FloatField(blank=False, default=0)
    carbohydrates = models.FloatField(blank=False, default=0)
    calories = models.FloatField(blank=False, default=0)
    price = models.DecimalField(blank=False, default=1, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    product = models.ForeignKey(Product, related_name='ingredient_product', blank=False)
    amount = models.FloatField(default=1, blank=False)
    dish = models.ForeignKey(Dish, related_name='ingredient_dish', blank=False)

    def __str__(self):
        return str(self.product) + "->" + str(self.dish)


class Order(models.Model):
    client = models.ForeignKey(User, related_name='order_client', blank=True)
    address = models.ForeignKey(Address, related_name='order_address', blank=True)
    date = models.DateTimeField(default=datetime.now)
    delivery = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ". " + str(self.client) + " (" + str(self.date) + ")"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_item_order', blank=False)
    dish = models.ForeignKey(Dish, related_name='order_item_dish')

    def __str__(self):
        return str(self.dish) + "->" + str(self.order.id)


class Table(models.Model):
    name = models.CharField(max_length=64, blank=False)
    places = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    client = models.ForeignKey(User, related_name='reservation_client', blank=True)
    table = models.ForeignKey(Table, related_name='reservation_table')
    order = models.ForeignKey(Order, related_name='reservation_order')
    date = models.DateTimeField(blank=False)

    def __str__(self):
        return str(self.table) + " - " + str(self.client) + " : " + str(self.date)

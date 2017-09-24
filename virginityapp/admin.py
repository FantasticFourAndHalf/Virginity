from django.contrib import admin

# Register your models here.

# login: admin
# pass: reb0rnapp
import virginityapp.models as virginityapp

from django.contrib.auth.models import Group

admin.site.unregister(Group)


class IngredientInline(admin.TabularInline):
    model = virginityapp.Ingredient
    extra = 1


class OrderItemInline(admin.TabularInline):
    model = virginityapp.OrderItem
    extra = 1


class DishImagesInline(admin.TabularInline):
    model = virginityapp.DishImage
    extra = 1


class TaggedInline(admin.TabularInline):
    model = virginityapp.Tagged
    extra = 1


@admin.register(virginityapp.Dish)
class DishModel(admin.ModelAdmin):
    icon = '<i class="material-icons">local_dining</i>'
    inlines = [IngredientInline, DishImagesInline, TaggedInline]


# @admin.register(virginityapp.DishImage)
# class DishImageModel(admin.ModelAdmin):
#     icon = '<i class="material-icons">add_a_photo</i>'


@admin.register(virginityapp.User)
class UserModel(admin.ModelAdmin):
    icon = '<i class="material-icons">face</i>'


@admin.register(virginityapp.Address)
class AddressModel(admin.ModelAdmin):
    icon = '<i class="material-icons">home</i>'


@admin.register(virginityapp.Product)
class ProductModel(admin.ModelAdmin):
    icon = '<i class="material-icons">spa</i>'


@admin.register(virginityapp.Order)
class OrderModel(admin.ModelAdmin):
    icon = '<i class="material-icons">assignment</i>'
    inlines = [OrderItemInline]


@admin.register(virginityapp.Table)
class TableModel(admin.ModelAdmin):
    icon = '<i class="material-icons">layers</i>'


@admin.register(virginityapp.Reservation)
class ReservationModel(admin.ModelAdmin):
    icon = '<i class="material-icons">weekend</i>'


@admin.register(virginityapp.Tag)
class TagModel(admin.ModelAdmin):
    icon = '<i class="material-icons">local_offer</i>'

from django.contrib import admin

# Register your models here.

# login: admin
# pass: reb0rnapp
import virginityapp.models as virginityapp

admin.site.register(virginityapp.User)
admin.site.register(virginityapp.Address)
admin.site.register(virginityapp.Product)
admin.site.register(virginityapp.Dish)
admin.site.register(virginityapp.Ingredient)
admin.site.register(virginityapp.Order)
admin.site.register(virginityapp.OrderItem)
admin.site.register(virginityapp.Table)
admin.site.register(virginityapp.Reservation)

from django.contrib import admin

from . import models

# Register your models here.

admin.register(models.Collection)
admin.register(models.Product)
admin.register(models.Order)
admin.register(models.OrderItem)
admin.register(models.Customer)
admin.register(models.Address)
admin.register(models.Cart)
admin.register(models.CartItem)
admin.register(models.Promotion)
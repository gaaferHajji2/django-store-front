from django.contrib import admin

from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'unit_price', 'inventory_status', 'collection_title']

    list_editable = [ 'unit_price' ]

    list_per_page = 10

    list_select_related = ['collection']

    @admin.display(ordering='inventory')
    def inventory_status(self, product: models.Product):
        if product.inventory < 10:
            return 'Low'
        
        return 'OK'
    
    @admin.display(ordering='collection__title')
    def collection_title(self, product: models.Product):
        return product.collection.title

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [ 'first_name', 'last_name', 'membership' ]

    list_editable = [ 'membership' ]

    list_per_page = 10

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'placed_at', 'customer' ]

    list_per_page = 10

# Register your models here.

# admin.site.register(models.Collection)
admin.site.register(models.Product, ProductAdmin)
# admin.site.register(models.Order)
admin.site.register(models.OrderItem)
# admin.site.register(models.Customer)
admin.site.register(models.Address)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)
admin.site.register(models.Promotion)
from django.contrib import admin

from django.db.models import QuerySet

from django.db.models.aggregates import Count

from django.utils.html import format_html, urlencode

from django.urls import reverse

from . import models

class InventoryFilter(admin.SimpleListFilter):

    title = "Inventory"
    
    parameter_name = "Inventory"

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low'),
            ('>=10', 'OK')
        ]
    
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
        elif self.value() == '>=10':
            return queryset.filter(inventory__gte=10)

class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'unit_price', 'inventory_status', 'collection_title']

    list_editable = [ 'unit_price' ]

    list_filter = [ 'collection', 'last_update', InventoryFilter ]

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
    list_display = [ 'id', 'title', 'products_count' ]

    list_per_page = 5

    @admin.display(ordering='products_count')
    def products_count(self, collection):

        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            })
        )

        return format_html('<a href="{}">{}</a>', url, collection.products_count)
    
    # In This Way We Can Override The Default Query Set
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [ 'first_name', 'last_name', 'membership', 'orders' ]

    list_editable = [ 'membership' ]

    list_per_page = 10

    search_fields = [ 'first_name__istartswith', 'last_name__istartswith' ]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders=Count('order')
        )

    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist') 
            + '?'
            + urlencode({
                'customer__id': customer.id
            })
        )

        return format_html('<a href="{}">{}</a>', url, customer.orders)

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
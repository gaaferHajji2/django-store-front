from django.contrib import admin

from django.contrib.contenttypes.admin import GenericTabularInline

from store.admin import ProductAdmin

from store.models import Product

from tags.models import TaggedItem

# Register your models here.
class TagInline(GenericTabularInline):
    model = TaggedItem

    min_num = 1

    max_num = 10

    extra = 0

    autocomplete_fields = ['tag']

class CustomProductAdmin(ProductAdmin):
    inlines = [ TagInline ]

admin.site.unregister(Product)

admin.site.register(Product, CustomProductAdmin)
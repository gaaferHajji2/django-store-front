from django.shortcuts import render
# from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField

from django.db.models.aggregates import Count, Sum, Max, Min, Avg

from django.db.models.functions import Concat

from django.contrib.contenttypes.models import ContentType

from store.models import Product, OrderItem, Order, Customer, Collection

from tags.models import TaggedItem

# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello World') 

    # query_set = Product.objects.all() 

    try:
        product = Product.objects.get(id=1) 
    
        # print("The Query Data Is: ", product.title) 
    except ObjectDoesNotExist as e:
        print("Exception Occurred-01: ", e.__str__())  
    
    try:
        product_2 = Product.objects.get(pk=0) 
    
        # print("The Query Data With Pk is: ", product_2.title) 
    except ObjectDoesNotExist as e:
        print("Exception Occurred-02: ", e.__str__()) 

    

    # for product in query_set:
    #     print("The Product Is: ", product) 

    return render(request, 'hello.html', { 'name': 'Jafar Loka'}) 
    # return render(request, 'hello.html') 

def say_hello_2(request):
    product = Product.objects.filter(pk=3).first() 

    exists = Product.objects.filter(pk=0).exists() 


    print("\t\t", "-"*25) 

    if product is None:
        print("No Product Found") 
    
    # print("The Product Data Is: ", product.description) 
    # print("The Check Of Product Exists is: ", exists) 

    product_query_set = Product.objects.filter(unit_price__gt=20) 
    product_query_set_02 = Product.objects.filter(unit_price__lte=20) 

    # print("The Data Of Product Query Set Is: ", product_query_set) 
    # print("The Data Of Product Query Set Is: ", product_query_set_02) 

    product_query_set_03 = Product.objects.filter(unit_price__range=(20, 30)) 

    print("The Data Of Product Query Set Range Is: ", product_query_set_03) 

    print("\t\t", "-"*25) 


    return render(request, 'hello.html', 
        { 'name': 'Jafar Loka-02', 'products': list(product_query_set_03)}) 

def say_hello_3(request):
    # product_query_set_with_collection = Product.objects.filter(collection_id=2).query 
    product_query_set_with_collection = Product.objects.filter(collection__id=6) 
    # product_query_set_with_collection = Product.objects.filter(collection__id__range=(4, 6)) 

    # print("The Count Of Data Is: ", product_query_set_with_collection)

    return render(request, 'hello.html', 
        {   'name': 'Jafar Loka Test Relation', 
            'products': list(product_query_set_with_collection)
        }
    )

def say_hello_4(request):
    product_query_set_with_collection = Product.objects.filter(title__contains='fruit') 

    return render(request, 'hello.html', 
        {   'name': 'Jafar Loka Test Contains', 
            'products': list(product_query_set_with_collection)
        }
    )

def say_hello_5(request):
    product_query_set_with_collection = Product.objects.filter(title__icontains='coffee') 

    return render(request, 'hello.html', 
        {   'name': 'Jafar Loka Test iContains', 
            'products': list(product_query_set_with_collection)
        }
    )

def say_hello_6(request):
    product_query_set_with_collection = Product.objects.filter(last_update__year=2021) 

    return render(request, 'hello.html', 
        {   'name': 'Jafar Loka Test last update With Year', 
            'products': list(product_query_set_with_collection)
        }
    )

def say_hello_7(request):
    product_query_set_with_collection = Product.objects.filter(description__isnull=True) 

    return render(request, 'hello.html', 
        {   'name': 'Jafar Loka Test last update With Year', 
            'products': list(product_query_set_with_collection)
        }
    )

def say_hello_8(request):
    products_query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20) 

    return render(request, 'hello.html', { 'products': products_query_set, 'name': 'Jafar Loka'}) 

def say_hello_9(request):
    products_query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20) 

    return render(request, 'hello.html', { 'products': products_query_set, 'name': 'Jafar Loka'}) 

def say_hello_10(request):
    products_query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20)) 

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products': products_query_set}) 

def say_hello_11(request):
    products_query_set = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20)) 

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products': products_query_set}) 

def say_hello_12(request):
    # products_query_set = Product.objects.filter(inventory=F('unit_price')) 
    products_query_set = Product.objects.filter(inventory=F('collection__id')) 

    return render(request, 'hello.html', 
        { 'name': 'Jafar Loka Test F-Class', 'products': products_query_set}
    ) 

def say_hello_13(request):
    products_query_set = Product.objects.order_by('unit_price', '-title') 

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products': products_query_set}) 

def say_hello_14(request):
    products_query_set = Product.objects.order_by('unit_price', '-title').reverse() 

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products': products_query_set}) 

def say_hello_15(request):
    products_query_set = Product.objects.filter(collection__id=6).order_by('unit_price') 

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products': products_query_set}) 

def say_hello_16(request):
    product = Product.objects.earliest('unit_price') 
    product_2 = Product.objects.latest('unit_price') 

    print("The Product Title Is: ", product.title) 

    print("The Product-02 Title Is: ", product_2.title) 

    return render(request, 'hello.html', { 'name': 'Jafar Loka' }) 

def say_hello_17(request):
    products_query_set = Product.objects.order_by('unit_price', '-title')[:5] 

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products': products_query_set}) 

def say_hello_18(request):
    products_query_set = Product.objects.order_by('unit_price', '-title')[5:10] 

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products': products_query_set}) 

def say_hello_19(request):
    products_query_set = Product.objects.values('id', 'title')

    print("The Query For Select Specific Fields Is: ", products_query_set.query)

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products': products_query_set}) 

def say_hello_20(request):
    # This Will Return Dict When Evaluated
    products_query_set = Product.objects.values('id', 'title', 'collection__title')

    # print("The Query For Select Specific Fields Is: ", products_query_set.query)

    # print("The First Product Is: ", products_query_set[0])

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products': products_query_set})

def say_hello_21(request):
    # This Will Return Tuple Of Values When Evaluated
    # id --> result_tuple[0]
    # title --> result_tuple[1]
    # collection__title --> result_tuple[2]
    products_query_set = Product.objects.values_list('id', 'title', 'collection__title')

    # print("The Query For Select Specific Fields Is: ", products_query_set.query)

    # print("The First Product Is: ", products_query_set[0])

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products_list': products_query_set})

def say_hello_22(request):
    # When We Create Relation Between OrderItem And Product, Django Will Create
    # product_id Column At Runtime.
    order_item_queryset = OrderItem.objects.values('product_id').distinct()
    # order_item_queryset = OrderItem.objects.values('product__id').distinct()

    # print("The First Order Item Is: ", order_item_queryset[0])

    products_queryset = Product.objects.values('id', 'title')\
        .filter(id__in=order_item_queryset)\
        .order_by('title')

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products_list': products_queryset })

def say_hello_23(request):
    products_queryset = Product.objects.select_related('collection').all()

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products_list': products_queryset })

def say_hello_24(request):
    products_queryset = Product.objects.prefetch_related('promotions').all()

    print("The Query Using prefetch_related Is: ", products_queryset)

    return render(request, 'hello.html', { 'name': 'Jafar Loka' })

def say_hello_25(request):
    # orderitem_set Will Be Created From Django AS Reverse Of Relationships
    orders_queryset = Order.objects\
        .select_related('customer')\
        .prefetch_related('orderitem_set__product')\
        .order_by('-placed_at')[:5]
    
    # print("The Orders Query Set Is: ", orders_queryset[0])
    
    return render(request, 'hello.html', { 'name': 'Jafar Loka ', 'orders': orders_queryset })

def say_hello_26(request):
    products_count = Product.objects\
        .aggregate(
            Count('id'), 
            count=Count('id'), 
            min_price=Min('unit_price'),
            max_price=Max('unit_price'),
        )

    return render(request, 'hello.html', { 
        'products_count': products_count, 
        'name': 'Jafar-Loka',
    })

def say_hello_27(request):
    result_1 = Order.objects.aggregate(count=Count('id'))

    result_2 = OrderItem.objects.filter(product__id = 1).aggregate(units_sold=Sum('quantity'))

    result_3 = Order.objects.filter(customer__id=1).aggregate(count=Count('id'))

    result_4 = Product.objects.filter(collection__id = 3)\
    .aggregate(
        min_price   =Min('unit_price'), 
        avg_price   = Avg('unit_price'), 
        max_price   =Max('unit_price'))
    
    return render(request, 'hello.html', {
        'name': 'Jafar Loka',
        'result_1': result_1,
        'result_2': result_2,
        'result_3': result_3,
        'result_4': result_4
    })

def say_hello_28(request):
    queryset = Customer.objects.annotate(
        is_new=Value(True), 
        new_id=F('id') + 1,
        full_name= Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'),
        full_name_02 = Concat('first_name', Value(' '), 'last_name')
    )

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'customers': queryset })

def say_hello_29(request):

    queryset = Customer.objects.annotate(
        is_new=Value(True), 
        new_id=F('id') + 1,
        full_name= Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'),
        full_name_02 = Concat('first_name', Value(' '), 'last_name'),
        order_count = Count('order'))

    # print("The First Object Is: ", queryset[0].__dict__)

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'customers': queryset })

def say_hello_30(request):
    queryset = Product.objects.annotate(
        discount_price = ExpressionWrapper(
            F('unit_price') * 0.8, 
            output_field=DecimalField())
    )

    # print("The First Object Is: ", queryset[0].__dict__)

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'products_02': queryset })

def say_hello_31(request):
    
    taggedItem = TaggedItem.objects.get_tags_for(Product, 1)

    return render(request, 'hello.html', {'name': 'Jafar Loka', 'tagsItem': taggedItem})

def save_collection_example_1(request):
    collection = Collection()

    collection.title = "Video Games-05"

    collection.featured_product = Product(pk=1)

    collection.save()

    # collection = collection.objects.select_related('featured_product')

    print("The New Collection Is: ", collection.__dict__)

    return render(request, 'hello.html', { 'name': 'Jafar Loka', 'collection': collection })

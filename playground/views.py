from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F

from store.models import Product

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


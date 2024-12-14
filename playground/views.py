from django.shortcuts import render

from django.http import HttpResponse

from django.core.exceptions import ObjectDoesNotExist;

from store.models import Product

# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello World');

    # query_set = Product.objects.all();

    try:
        product = Product.objects.get(id=1);
    
        print("The Query Data Is: ", product.title);
    except ObjectDoesNotExist as e:
        print("Exception Occurred-01: ", e.__str__());
    
    try:
        product_2 = Product.objects.get(pk=0);
    
        print("The Query Data With Pk is: ", product_2.title);
    except ObjectDoesNotExist as e:
        print("Exception Occurred-02: ", e.__str__());

    

    # for product in query_set:
    #     print("The Product Is: ", product);

    return render(request, 'hello.html', { 'name': 'Jafar Loka'});
    # return render(request, 'hello.html');

def say_hello_2(request):
    product = Product.objects.filter(pk=3).first();

    exists = Product.objects.filter(pk=0).exists();


    print("\t\t", "-"*25);

    if product is None:
        print("No Product Found");
    
    print("The Product Data Is: ", product.description);
    print("The Check Of Product Exists is: ", exists);

    product_query_set = Product.objects.filter(unit_price__gt=20);
    product_query_set_02 = Product.objects.filter(unit_price__lte=20);

    # print("The Data Of Product Query Set Is: ", product_query_set);
    # print("The Data Of Product Query Set Is: ", product_query_set_02);

    product_query_set_03 = Product.objects.filter(unit_price__range=(20, 30));

    print("The Data Of Product Query Set Range Is: ", product_query_set_03);

    print("\t\t", "-"*25);


    return render(request, 'hello.html', 
        { 'name': 'Jafar Loka-02', 'products': list(product_query_set_03)});

def say_hello_3(request):
    # product_query_set_with_collection = Product.objects.filter(collection_id=2).query;
    product_query_set_with_collection = Product.objects.filter(collection__id=6);
    # product_query_set_with_collection = Product.objects.filter(collection__id__range=(4, 6));

    # print("The Count Of Data Is: ", product_query_set_with_collection)

    return render(request, 'hello.html', 
        {   'name': 'Jafar Loka Test Relation', 
            'products': list(product_query_set_with_collection)
        }
    )

def say_hello_4(request):
    product_query_set_with_collection = Product.objects.filter(title__contains='fruit');

    return render(request, 'hello.html', 
        {   'name': 'Jafar Loka Test Contains', 
            'products': list(product_query_set_with_collection)
        }
    )

def say_hello_5(request):
    product_query_set_with_collection = Product.objects.filter(title__icontains='coffee');

    return render(request, 'hello.html', 
        {   'name': 'Jafar Loka Test iContains', 
            'products': list(product_query_set_with_collection)
        }
    )

def say_hello_6(request):
    product_query_set_with_collection = Product.objects.filter(last_update__year=2021);

    return render(request, 'hello.html', 
        {   'name': 'Jafar Loka Test last update With Year', 
            'products': list(product_query_set_with_collection)
        }
    )

def say_hello_7(request):
    product_query_set_with_collection = Product.objects.filter(description__isnull=True);

    return render(request, 'hello.html', 
        {   'name': 'Jafar Loka Test last update With Year', 
            'products': list(product_query_set_with_collection)
        }
    )
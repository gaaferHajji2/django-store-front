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
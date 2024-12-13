from django.shortcuts import render

from django.http import HttpResponse

from store.models import Product

# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello World');

    query_set = Product.objects.all();

    for product in query_set:
        print("The Product Is: ", product);

    return render(request, 'hello.html', { 'name': 'Jafar Loka'});
    # return render(request, 'hello.html');
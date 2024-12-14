from django.shortcuts import render

from django.http import HttpResponse

from store.models import Product

# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello World');

    # query_set = Product.objects.all();

    query_data = Product.objects.get(id=1);
    query_data_2 = Product.objects.get(pk=2);

    print("The Query Data Is: ", query_data.title);
    print("The Query Data With Pk is: ", query_data_2.title);

    # for product in query_set:
    #     print("The Product Is: ", product);

    return render(request, 'hello.html', { 'name': 'Jafar Loka'});
    # return render(request, 'hello.html');
from django.shortcuts import get_object_or_404

from django.db.models import F

from django.db.models.aggregates import Count

# from django.http import HttpResponse

from rest_framework import status

from rest_framework.viewsets import ModelViewSet

# from rest_framework.views import APIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from rest_framework.mixins import ListModelMixin, CreateModelMixin

# from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Product, Collection

from .serializers import ProductSerializer, CollectionSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('collection').all()

    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return { 'request': self.request }
    
    def delete(self, request, pk: int):
        product = get_object_or_404(Product, pk=pk)

        if product.orderitems.count() > 0:
            return Response({'error': 'product cannot be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductList(ListCreateAPIView):

    # queryset = Product.objects.select_related('collection').all()

    # serializer_class = ProductSerializer
    
    # def get_serializer_context(self):
    #     return { 'request': self.request }

    # def get(self, request):
    #     queryset = 
    #     serializer = ProductSerializer(queryset, many=True, context={ 'request': request })

    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = (data = request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ProductDetail(RetrieveUpdateDestroyAPIView):

    # queryset = Product.objects.all()

    # serializer_class = ProductSerializer

    # def get(self, request, id: int):
    #     product = get_object_or_404(Product, pk=id)
    #     serializer = ProductSerializer(product, context={ 'request': request })
    #     return Response(serializer.data)
    
    # def put(self, request, id: int):
    #     product = get_object_or_404(Product, pk=id)

    #     serializer = ProductSerializer(product, data = request.data);
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data)
    
    # def delete(self, request, pk: int):
    #     product = get_object_or_404(Product, pk=pk)

    #     if product.orderitems.count() > 0:
    #         return Response({'error': 'product cannot be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    #     product.delete()

    #     return Response(status=status.HTTP_204_NO_CONTENT)

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()

    serializer_class = CollectionSerializer

    def delete(self, request, pk: int):
        collection = get_object_or_404(
            Collection.objects.annotate(products_count=Count('products')), 
            pk=pk
        )

        if collection.products.count() > 0:
            return Response({'error': 'Collection Cannot Be Deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        collection.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# class CollectionList(ListCreateAPIView):

#     queryset = Collection.objects.annotate(products_count=Count('products')).all()

#     serializer_class = CollectionSerializer

    # def get(self, request):
    #     queryset = Collection.objects.annotate(products_count=Count('products')).all();
    #     serializer = CollectionSerializer(queryset, many=True)

    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = CollectionSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

class CollectionDetail(RetrieveUpdateDestroyAPIView):

    queryset = Collection.objects.annotate(products_count=Count('products')).all()

    serializer_class = CollectionSerializer

    # lookup_field = 'id'

    # def get(self, request, pk: int):
    #     collection = get_object_or_404(
    #         Collection.objects.annotate(products_count=Count('products')), 
    #         pk=pk
    #     )

    #     serializer = CollectionSerializer(collection)

    #     return Response(serializer.data)
    
    # def put(self, request, pk: int):
    #     collection = get_object_or_404(
    #         Collection.objects.annotate(products_count=Count('products')), 
    #         pk=pk
    #     )

    #     serializer = CollectionSerializer(collection, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data)
    
    def delete(self, request, pk: int):
        collection = get_object_or_404(
            Collection.objects.annotate(products_count=Count('products')), 
            pk=pk
        )

        if collection.products.count() > 0:
            return Response({'error': 'Collection Cannot Be Deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        collection.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
# @api_view(['GET', 'POST'])
# def product_list(request):
#         
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, id):

# @api_view(['GET', 'POST'])
# def collection_list(request):

# @api_view(['GET', 'PUT', 'DELETE'])
# def collection_detail(request, pk: int):
from django.shortcuts import get_object_or_404

# from django.db.models import F

from django.db.models.aggregates import Count

# from django.http import HttpResponse

from rest_framework import status

from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin

from rest_framework.viewsets import ModelViewSet, GenericViewSet

from rest_framework.permissions import IsAuthenticated

# from rest_framework.views import APIView

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from rest_framework.mixins import ListModelMixin, CreateModelMixin

# from rest_framework.decorators import 
from rest_framework.decorators import action

from rest_framework.response import Response

from rest_framework.filters import SearchFilter, OrderingFilter

# from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from core.serializers import UserSerializer
from store.permissions import CanViewHistory, IsAdminOrReadOnly, IsCustomerServiceOnly

# from core import serializers

from .models import CartItem, Customer, Product, Collection, OrderItem, Review, Cart

from .filters import ProductFilter

from .serializers import AddCartItemSerialzier, CartItemSerializer, CustomerSerializer, ProductSerializer, CollectionSerializer, ReviewSerializer, CartSerializer, UpdateCartItemSerializer

from .pagination import DefaultPagination

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['collection_id']
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]

    # def get_queryset(self):
    #     queryset = Product.objects.all()

    #     # This Will Produce Error If We Don't Set collection_id With URL
    #     # collection_id = self.request.query_params['collection_id']
    #     collection_id = self.request.query_params.get('collection_id')

    #     if collection_id is not None:
    #         queryset = queryset.filter(collection_id=collection_id)
        
    #     return queryset


    def get_serializer_context(self):
        return { 'request': self.request }
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id = kwargs['pk']).count() > 0:
            return Response({'error': 'product cannot be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *args, *kwargs)


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
    permission_classes = [IsAdminOrReadOnly]
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Collection Cannot Be Deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class ReviewViewSet(ModelViewSet):
    
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self): # type: ignore
        return Review.objects.filter(product_id = self.kwargs['product_pk'])

    def get_serializer_context(self):
        return { 'product_id': self.kwargs['product_pk'] }

class CartViewSet( CreateModelMixin, 
                   RetrieveModelMixin, 
                   DestroyModelMixin, 
                   GenericViewSet
                ):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):

    # serializer_class = CartItemSerializer

    # This list must be in lower case
    http_method_names = ['get', 'post', 'patch', 'delete'];

    def get_serializer_class(self): # type: ignore
        if self.request.method == 'POST':
            return AddCartItemSerialzier
        
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        
        return CartItemSerializer

    def get_queryset(self): # type: ignore
        return CartItem.objects.filter(cart_id = self.kwargs['cart_pk']).select_related('product')
    
    def get_serializer_context(self):
        return { 'cart_id': self.kwargs['cart_pk'] }

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

# class CollectionDetail(RetrieveUpdateDestroyAPIView):

#     queryset = Collection.objects.annotate(products_count=Count('products')).all()

#     serializer_class = CollectionSerializer

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
    
    # def delete(self, request, pk: int):
    #     collection = get_object_or_404(
    #         Collection.objects.annotate(products_count=Count('products')), 
    #         pk=pk
    #     )

    #     if collection.products.count() > 0:
    #         return Response({'error': 'Collection Cannot Be Deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    #     collection.delete()

    #     return Response(status=status.HTTP_204_NO_CONTENT)


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

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsCustomerServiceOnly]

    # here we return Objects not classes
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
        
    #     return [IsAuthenticated()]

    @action(detail=True, permission_classes=[CanViewHistory])
    def view_history(self, request, pk):
        return Response({
            "user": UserSerializer(request.user).data,
            "pk": pk
        })

    # Here also we can add permission_classes to action-decorator as list
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        # customer = Customer.objects.select_related('user').get(user_id = request.user.id)
        customer = get_object_or_404(Customer.objects.select_related('user'), user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
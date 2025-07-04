from rest_framework import serializers

from decimal import Decimal

from .models import CartItem, Product, Collection, Review, Cart

# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length= 255)

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

#     # collection = serializers.PrimaryKeyRelatedField(queryset = Collection.objects.all())

#     # collection = serializers.StringRelatedField()
#     # collection = CollectionSerializer()

#     collection = serializers.HyperlinkedRelatedField(
#         queryset = Collection.objects.all(),
#         view_name = 'collection-detail',
#     )

#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.1)

class CollectionSerializer(serializers.ModelSerializer):

    products_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    # products_count = serializers.SerializerMethodField(method_name='get_products_count')

    # def get_products_count(self, collection: Collection):
    #     return collection.products_count

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']

    # price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'date']
    
    def create(self, validated_data):
        product_id = self.context['product_id']

        return Review.objects.create(product_id=product_id, **validated_data)

class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields= ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        # Here We Define items Inside The CartItem-Model AS The Related Name
        fields = [ 'id', 'items']


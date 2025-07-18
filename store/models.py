from django.db import models

from django.core.validators import MinValueValidator

from uuid import uuid4

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount    = models.FloatField()

    # Also Here We Can Set Start And End Date For Each Promotion

class Collection(models.Model):
    title = models.CharField(max_length=255, unique=True)

    featured_product = models.ForeignKey(
        to='Product', on_delete=models.SET_NULL, null=True, related_name='+'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class Product(models.Model):
    title = models.CharField(max_length=255)

    slug  = models.SlugField()

    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[
            MinValueValidator(limit_value=1, message="Unite Price Must Be geater Than Or Equal 1$")
        ]
    )
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

    collection = models.ForeignKey(to=Collection, on_delete=models.PROTECT, related_name='products')

    # promotions = models.ManyToManyField(to=Promotion, related_name='products')
    promotions = models.ManyToManyField(to=Promotion, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.title
    
    class Meta:
        ordering = ['title']

class Customer(models.Model):

    MEMBERSHIP_BRONZE = 'B'

    MEMBERSHIP_SLIVER = 'S'

    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SLIVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]

    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    email      = models.EmailField(unique=True)
    phone      = models.CharField(max_length=13)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['first_name', 'last_name']

class Order(models.Model):
    PAYMENT_STATUS_PENDING  = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED   = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)

    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)

    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT)
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city   = models.CharField(max_length=255)

    customer = models.OneToOneField(to=Customer, on_delete=models.CASCADE, primary_key=True)

class Cart(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='items', default=None)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['cart', 'product']]

class Review(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
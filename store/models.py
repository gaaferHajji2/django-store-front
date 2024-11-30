from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, unique=True);
    description = models.TextField();
    price = models.DecimalField(max_digits=6, decimal_places=2);
    inventory = models.IntegerField();
    last_update = models.DateTimeField(auto_now=True);

class Customer(models.Model):

    MEMBERSHIP_BRONZE = 'B';

    MEMBERSHIP_SLIVER = 'S';

    MEMBERSHIP_GOLD = 'G';

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SLIVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ];

    first_name = models.CharField(max_length=255);
    last_name  = models.CharField(max_length=255);
    email      = models.EmailField(unique=True);
    phone      = models.CharField(max_length=10);
    birth_date = models.DateField(null=True);
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE);

class Order(models.Model):
    PENDING_STATUS  = 'P';
    COMPLETE_STATUS = 'C';
    FAILED_STATUS   = 'F';

    ORDER_STATUS= [
        (PENDING_STATUS, 'Pending'),
        (COMPLETE_STATUS, 'Complete'),
        (FAILED_STATUS, 'Failed'),
    ];

    placed_at = models.DateTimeField(auto_now_add=True);

    payment_status = models.CharField(max_length=1, choices=ORDER_STATUS, default=PENDING_STATUS);


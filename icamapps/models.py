from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from icamiam.settings import AUTH_USER_MODEL
import uuid
from django.conf import settings 


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    image =  models.ImageField(upload_to='products/', null=True, blank=True)


    def __str__(self):
        return self.name
    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if not self.image:
            self.image = None  # Définir l'image sur None si elle est vide

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    order_number = models.CharField(max_length=12, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = str(uuid.uuid4().int)[:12]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} {self.product.name} - {self.order_number}"

    @property
    def total_price(self):
        return self.product.price * self.quantity

class Panier(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=None)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
    
    @property
    def total_items(self):
        return sum(order.quantity for order in self.orders.all())
    
class Confirmation(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import AbstractUser

class General(models.Model):
    class Meta:
        abstract = True
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Seller(General):
    name = models.CharField(max_length=256)
    address = models.TextField()
    certificate_code = models.CharField(max_length=10)


class Pineapple(General):
    price_toman = models.PositiveIntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='pineapple_seler')


class Order(General):
    pineapple = models.ForeignKey(Pineapple, on_delete=models.CASCADE, related_name='pineapple_seler')
    name = models.CharField(max_length=50)
    weight_kg = models.FloatField()
    

class Comment(General):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()


class Subscription(General):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)

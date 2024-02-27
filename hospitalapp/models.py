from django.db import models


# Create your models here.

class users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField(null=True)
    password = models.CharField(max_length=100)
    date = models.DateField(null=True)

    def __str__(self):
        return self.username


class products(models.Model):
    products_name = models.CharField(max_length=200)
    products_price = models.CharField(max_length=200)
    product_quantity = models.IntegerField(null=True)

    def __str__(self):
        return self

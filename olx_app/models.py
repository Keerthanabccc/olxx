from django.db import models

# Create your models here.

class product_model(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    colour = models.CharField(max_length=30)

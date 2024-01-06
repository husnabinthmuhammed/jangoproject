from django.db import models

# Create your models here.

class Products(models.Model):
    pdt_name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.CharField(max_length=400)
    user = models.CharField(max_length=300, default='')
    quantity = models.IntegerField(default=1, blank=True, null=True)


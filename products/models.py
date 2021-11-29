from django.db import models
from django.db.models.fields import DecimalField


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = DecimalField(decimal_places=2, max_digits=1000)
    summery = models.TextField()

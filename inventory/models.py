from django.db import models

# Create your models here.

class Inventory(models.Model):
    product_name=models.CharField(max_length=20)
    product_details= models.CharField(max_length=45)
    quantity=models.IntegerField()
    vendor_name=models.CharField(max_length=25)
    destination=models.CharField(max_length=70)
    comments=models.CharField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    
    
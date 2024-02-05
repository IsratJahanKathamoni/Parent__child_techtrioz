from django.db import models


class Person_name(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40, blank=True,null=True)
    contact  = models.IntegerField(max_length=15)
    details =models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.first_name
    
    
    
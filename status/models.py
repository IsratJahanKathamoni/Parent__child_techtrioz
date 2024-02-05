from django.db import models

# Create your models here.

class Status(models.Model):
    root=models.CharField(max_length=30,null=True, blank=True)
    child_name=models.CharField(max_length=30,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return self.child_name

class Child(models.Model):

  upper_parent= models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True)
  parent_name= models.ForeignKey('Child', on_delete=models.SET_NULL, null=True, blank=True)
  child_name=models.CharField(max_length=30, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
          return self.child_name


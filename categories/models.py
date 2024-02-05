



from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    category_name = models.CharField(max_length=55)
    #, null=False, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name
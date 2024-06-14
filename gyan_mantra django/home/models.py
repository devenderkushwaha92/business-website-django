from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    mobile=models.CharField(max_length=20)
    Class=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

from django.db import models



# Create your models here.



class Index (models.Model):
    name=models.CharField(max_length=122)
    last=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    user=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    confirm=models.CharField(max_length=50)
    Address=models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) ->str:
        return self.name+" "+self.last


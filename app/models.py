from django.db import models

# Create your models here.
class BMW(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    islike = models.BooleanField(default=True)

def __str__(self) -> str:
    return self.name
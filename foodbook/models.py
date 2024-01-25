from django.db import models

class Food(models.Model):
    name=models.CharField(max_length=200,unique=True)
    category=models.CharField(max_length=200)
    cuisine=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
 

 
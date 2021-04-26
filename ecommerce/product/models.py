from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title


class product(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Seller_Mobile= models.CharField(max_length=15)
    Price_Range= models.ForeignKey(Position,on_delete=models.CASCADE)



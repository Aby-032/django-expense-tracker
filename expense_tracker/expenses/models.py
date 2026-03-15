from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Category Table
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#Expense Table
class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
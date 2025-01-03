from django.db import models
from category.models import Category
class Product(models.Model):
    Product_name=models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    Discription=models.CharField(max_length=200,blank=True)
    price = models.IntegerField()
    image=models.ImageField(upload_to='photos/products')
    stocks= models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    create_date=models.DateTimeField(auto_now_add=True)
    modifield_date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.Product_name
from django.db import models

class Category (models.Model):
    Cagtegory_name=models.CharField(max_length=50,unique=True)
    slug=models.CharField(max_length=100,unique=True)
    descriptions=models.TextField(max_length=100,blank=True)
    cat_image=models.ImageField( upload_to= 'photos/chategories',blank= True)
    
    
    
    def __str__(self) :
        return self.Cagtegory_name
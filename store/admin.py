from django.contrib import admin

# Register your models here.
from .models import Product


class productAdmin(admin.ModelAdmin):
    
    list_display=('Product_name','price','stocks','category','modifield_date','is_available')
    prepopulated_fields = {'slug': ('Product_name',)}


admin.site.register(Product)
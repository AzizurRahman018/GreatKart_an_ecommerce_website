from django.contrib import admin
from . models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Cagtegory_name',)}
    list_display = ('Cagtegory_name','slug')

admin.site.register(Category,CategoryAdmin)
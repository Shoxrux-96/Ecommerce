from django.contrib import admin
from .models import Persons,Products
# Register your models here.
@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name','phoneNumber']
    list_filter = ['first_name']

# admin.site.register(Persons, PersonsAdmin)
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['user','name','price','create_time','status']
    list_filter = ['name','price','create_time',]
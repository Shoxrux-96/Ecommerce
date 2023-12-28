#myapp/serializers.py
from rest_framework import serializers
from .models import Persons, Products

class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.shortcuts import render
from .models import Persons,Products
from .serializers import ProductsSerializer
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Products.objects.all()[:6]
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ComputerPageView(TemplateView):
    template_name = 'computer.html'
    
class LaptopPageView(TemplateView):
    template_name = 'laptop.html'
    
class ProductPageView(TemplateView):
    template_name = 'product.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'

################     Persons API View       ###################
class PersonsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        persons = Persons.objects.all()
        serializer = PersonsSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PersonsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################    Products  API View       ###################
class ProductsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
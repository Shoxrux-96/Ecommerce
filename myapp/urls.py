# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonsAPIView, ProductsAPIView, ProductsViewSet
from myapp.views import HomePageView,AboutPageView,ComputerPageView,LaptopPageView,ProductPageView,ContactPageView

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path('about',AboutPageView.as_view(), name="aboutpage"),
    path('computer', ComputerPageView.as_view(), name="computerpage"),
    path('laptop', LaptopPageView.as_view(), name="laptoppage"),
    path('product', ProductPageView.as_view(), name="productpage"),
    path('contact', ContactPageView.as_view(), name="contactpage"),

    path('api/persons/', PersonsAPIView.as_view(), name='persons-api'),
    path('api/', include(router.urls)),
]
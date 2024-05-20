from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import Product
from .serializers import ProductSerializer


@extend_schema(responses=ProductSerializer)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

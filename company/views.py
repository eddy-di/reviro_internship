from rest_framework import generics, permissions

from company.models import Company, Product
from company.serializers import CompanySerializer, ProductSerializer


class CompanyListCreateView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [permissions.AllowAny]


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.filter()
    permission_classes = [permissions.AllowAny]


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()
    permission_classes = [permissions.AllowAny]

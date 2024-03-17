from rest_framework import generics, permissions

from company.models import Company, Product
from company.serializers import CompanySerializer, ProductSerializer


class CompanyListCreateView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [permissions.AllowAny]


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = 'company_id'


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = 'company_id'

    def get_queryset(self):
        company_id = self.kwargs.get(self.lookup_url_kwarg)
        queryset = Product.objects.filter(company=company_id)
        return queryset


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()  # filter(company='company_id')
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = 'product_id'

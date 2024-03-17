from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions

from company.models import Company, Product
from company.serializers import CompanySerializer, ProductSerializer


class CompanyListCreateView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary='Gets all companies.',
        description='Allows to `GET` a list of all companies in database, paginated to 10 instances per page.',
        tags=['Companies'],
        operation_id='company_list'
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary='Creates new company.',
        description='Allows to `POST` a new company.',
        request=CompanySerializer,
        tags=['Companies'],
        operation_id='company_create'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = 'company_id'

    @extend_schema(
        summary='Gets company.',
        description='Allows to `GET` a company from database.',
        tags=['Companies'],
        operation_id='company_retrieve'
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary='Partially updates company.',
        description='Allows to `PATCH` a company.',
        request=CompanySerializer,
        tags=['Companies'],
        operation_id='company_partial_update'
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        summary='Updates company.',
        description='Allows to `PUT` a company.',
        request=CompanySerializer,
        tags=['Companies'],
        operation_id='company_update'
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary='Deletes company.',
        description='Allows to `DELETE` a company.',
        tags=['Companies'],
        operation_id='company_destroy'
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = 'company_id'

    def get_queryset(self):
        company_id = self.kwargs.get(self.lookup_url_kwarg)
        queryset = Product.objects.filter(company=company_id)
        return queryset

    @extend_schema(
        summary='Gets all products.',
        description='Allows to `GET` all products related to `company_id` and paginates 10 instances per page.',
        tags=['Products']
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary='Creates new product.',
        description='Allows to `POST` a new product.',
        request=ProductSerializer,
        tags=['Products']
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()  # filter(company='company_id')
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = 'product_id'

    @extend_schema(
        summary='Gets a product.',
        description='Allows to `GET` a product.',
        tags=['Products']
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary='Partially updates product.',
        description='Allows to `PATCH` a product.',
        request=ProductSerializer,
        tags=['Products']
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        summary='Updates a product.',
        description='Allows to `PUT` a product.',
        request=ProductSerializer,
        tags=['Products']
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary='Deletes product.',
        description='Allows to `DELETE` a product.',
        tags=['Products']
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

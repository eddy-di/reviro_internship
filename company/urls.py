from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from company.views import (
    CompanyListCreateView,
    CompanyRetrieveUpdateDestroyView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
)

urlpatterns = [
    path(
        'companies',
        CompanyListCreateView.as_view(),
        name='companies'
    ),
    path(
        'companies/<int:pk>',
        CompanyRetrieveUpdateDestroyView.as_view(),
        name='company_details'
    ),
    path(
        'products',
        ProductListCreateView.as_view(),
        name='products'
    ),
    path(
        'products/<int:pk>',
        ProductRetrieveUpdateDestroyView.as_view(),
        name='product_details'
    ),
    # Spectacular schemas
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI
    path('swagger-ui', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

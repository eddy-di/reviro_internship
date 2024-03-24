from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from company.views import (
    CompanyListCreateView,
    CompanyRetrieveUpdateDestroyView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    UserRegisterView,
)

urlpatterns = [
    path(
        'companies',
        CompanyListCreateView.as_view(),
        name='companies'
    ),
    path(
        'companies/<int:company_id>',
        CompanyRetrieveUpdateDestroyView.as_view(),
        name='company_details'
    ),
    path(
        'companies/<int:company_id>/products',
        ProductListCreateView.as_view(),
        name='products'
    ),
    path(
        'companies/<int:company_id>/products/<int:product_id>',
        ProductRetrieveUpdateDestroyView.as_view(),
        name='product_details'
    ),
    # Spectacular schemas
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI
    path('swagger-ui', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Simple JWT auth
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    # Registration
    path('register', UserRegisterView.as_view(), name='register'),
]

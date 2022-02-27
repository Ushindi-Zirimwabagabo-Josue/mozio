from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Mozio API Docs",
      default_version='v1',
      description="Mozio API Docs",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="josueuzj9@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # path('', views.documentation, name='documentation'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('providers', views.ProviderAll.as_view(), name='provider-all'),
    path('providers/add', views.ProviderList.as_view(), name='provider-list'),
    path('providers/<int:pk>', views.ProviderDetail.as_view(), name='provider-detail'),
    path('serviceAreas', views.ServiceAreaAll.as_view(), name='service-area-all'),
    path('serviceAreas/add', views.ServiceAreaList.as_view(), name='service-area-list'),
    path('serviceAreas/<int:pk>', views.ServiceAreaDetail.as_view(), name='service-area-detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.documentation, name='documentation'),
    path('providers', views.ProviderAll.as_view(), name='provider-all'),
    path('providers/add', views.ProviderList.as_view(), name='provider-list'),
    path('providers/<int:pk>', views.ProviderDetail.as_view(), name='provider-detail'),
    path('serviceAreas', views.ServiceAreaAll.as_view(), name='service-area-all'),
    path('serviceAreas/add', views.ServiceAreaList.as_view(), name='service-area-list'),
    path('serviceAreas/<int:pk>', views.ServiceAreaDetail.as_view(), name='service-area-detail'),
]
from django.contrib import admin
from django.urls import path, include

from api.views import documentation, query

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', documentation),
    path('api/v1/', include("api.urls")),
    path('query/', query),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('platerak/', include('platerak.urls')),
    path('bezeroak/', include('bezeroak.urls')),
    path('admin/', admin.site.urls),
]

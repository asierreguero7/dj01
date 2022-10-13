from django.urls import path
from . import views

urlpatterns = [
    path('', views.bezeroak, name='bezeroak'),
    path('delete/<int:id>', views.delete, name='delete'),
]
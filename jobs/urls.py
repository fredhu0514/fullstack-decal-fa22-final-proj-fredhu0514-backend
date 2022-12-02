from django.urls import path, include
from rest_framework import routers
from .views import JobView, JobCreate


urlpatterns = [
    path(r'view/', JobView.as_view({'get': 'list'})),
    path('detail/<int:pk>/', JobView.as_view({'get': 'retrieve'})),
    path(r'post/', JobCreate.as_view({'post': 'create'})),
]
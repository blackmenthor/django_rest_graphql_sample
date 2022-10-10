from django.urls import path, include
from rest_framework import routers
from animal import views

router = routers.DefaultRouter()
router.register(r'animal', views.AnimalViewSet, basename='animal')

urlpatterns = [
    path('', include(router.urls)),
]

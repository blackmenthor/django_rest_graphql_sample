from django.urls import path, include
from rest_framework import routers
from gallery import views

router = routers.DefaultRouter()
router.register(r'gallery', views.AnimalGalleryViewSet, basename='animal_gallery')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework import routers
from keeper import views

router = routers.DefaultRouter()
router.register(r'animal_keeper', views.AnimalKeeperViewSet, basename='animal_keeper')

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import viewsets
from animal.models import Animal
from animal.serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_queryset(self, *args, **kwargs):
        return Animal.objects.all()

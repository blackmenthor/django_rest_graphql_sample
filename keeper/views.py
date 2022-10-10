from rest_framework import viewsets
from keeper.models import AnimalKeeper
from keeper.serializers import AnimalKeeperSerializer


class AnimalKeeperViewSet(viewsets.ModelViewSet):
    queryset = AnimalKeeper.objects.all()
    serializer_class = AnimalKeeperSerializer

    def get_queryset(self, *args, **kwargs):
        return AnimalKeeper.objects.all()

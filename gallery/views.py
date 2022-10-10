from rest_framework import viewsets
from gallery.models import AnimalGallery
from gallery.serializers import AnimalGallerySerializer


class AnimalGalleryViewSet(viewsets.ModelViewSet):
    queryset = AnimalGallery.objects.all()
    serializer_class = AnimalGallerySerializer

    def get_queryset(self, *args, **kwargs):
        return AnimalGallery.objects.all()

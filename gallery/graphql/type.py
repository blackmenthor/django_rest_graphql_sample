from graphene_django import DjangoObjectType
from gallery.models import AnimalGallery


class AnimalGalleryType(DjangoObjectType):
    class Meta:
        model = AnimalGallery
        fields = ('id', 'for_animal', 'for_keeper', 'image', 'created_date',
                  'modified_date')
        
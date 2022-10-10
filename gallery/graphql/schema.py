import graphene

from animal.models import Animal
from gallery.graphql.input import GalleryInput
from gallery.graphql.type import AnimalGalleryType
from gallery.models import AnimalGallery


class Query(graphene.ObjectType):
    galleries = graphene.List(AnimalGalleryType, input=GalleryInput(required=False))

    def resolve_galleries(root, info, input=None):
        try:
            if not input:
                return AnimalGallery.objects.all()
            if input.id_animal:
                return AnimalGallery.objects.filter(for_animal__id=input.id_animal)
            elif input.id_keeper:
                return AnimalGallery.objects.filter(for_animal__id=input.id_keeper)
            return AnimalGallery.objects.all()
        except Animal.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)

from graphene_django import DjangoObjectType

from keeper.models import AnimalKeeper


class AnimalKeeperType(DjangoObjectType):
    class Meta:
        model = AnimalKeeper
        fields = ('id', 'name', 'origin_country', 'animal', 'birth_date', 'image',
                  'created_date', 'modified_date')
        
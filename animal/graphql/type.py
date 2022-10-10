from graphene_django import DjangoObjectType

from animal.models import Animal


class AnimalType(DjangoObjectType):
    class Meta:
        model = Animal
        fields = ('id', 'name', 'image', 'created_date', 'modified_date')
        
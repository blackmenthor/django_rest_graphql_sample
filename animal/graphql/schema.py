import graphene

from animal.graphql.type import AnimalType
from animal.models import Animal


class ChangeAnimalName(graphene.Mutation):
    Output = AnimalType

    class Arguments:
        id = graphene.String(required=False)
        name = graphene.String(required=False)

    def mutate(self, info, id, name):
        animal = Animal.objects.get(id=id)
        animal.name = name
        return animal


class Mutation(graphene.ObjectType):
    change_animal_name = ChangeAnimalName.Field()


class Query(graphene.ObjectType):
    animals = graphene.List(AnimalType, name=graphene.String(required=False))

    def resolve_animals(root, info, name=None):
        try:
            if not name:
                return Animal.objects.all()
            return Animal.objects.filter(name__icontains=name)
        except Animal.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)

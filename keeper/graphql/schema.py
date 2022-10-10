import graphene

from animal.models import Animal
from keeper.graphql.type import AnimalKeeperType
from keeper.models import AnimalKeeper


class ChangeAnimalKeeperName(graphene.Mutation):
    Output = AnimalKeeperType

    class Arguments:
        id = graphene.String(required=False)
        name = graphene.String(required=False)

    def mutate(self, info, id, name):
        keeper = AnimalKeeper.objects.get(id=id)
        keeper.name = name
        return keeper


class Mutation(graphene.ObjectType):
    change_animal_keeper_name = ChangeAnimalKeeperName.Field()


class Query(graphene.ObjectType):
    keepers = graphene.List(AnimalKeeperType, name=graphene.String(required=False))

    def resolve_keepers(root, info, name=None):
        try:
            if not name:
                return AnimalKeeper.objects.all()
            return AnimalKeeper.objects.filter(name__icontains=name)
        except Animal.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)

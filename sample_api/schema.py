import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug

from animal.graphql import schema as AnimalSchema
from keeper.graphql import schema as AnimalKeeperSchema
from gallery.graphql import schema as AnimalGallerySchema


class Mutation(
    AnimalKeeperSchema.Mutation,
    AnimalSchema.Mutation,
    graphene.ObjectType,
):
    pass


class Query(
    AnimalKeeperSchema.Query,
    AnimalSchema.Query,
    AnimalGallerySchema.Query,
    graphene.ObjectType,
):
    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name="debug")
    else:
        pass


schema = graphene.Schema(query=Query, mutation=Mutation)

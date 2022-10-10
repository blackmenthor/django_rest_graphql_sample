import graphene


class GalleryInput(graphene.InputObjectType):
    id_animal = graphene.UUID(required=False)
    id_keeper = graphene.UUID(required=False)

from django.shortcuts import render
from graphene_django.views import GraphQLView


class CustomGraphQLView(GraphQLView):
    def render_graphiql(self, request, **data):
        if request:
            return render(request, "graphql_template.html", data)
        return super().render_graphiql(self, request, **data)

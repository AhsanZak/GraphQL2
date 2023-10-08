from django.urls import path
from graphene_django.views import GraphQLView
from quiz.schema import schema

# urlpatterns = [
#     path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
# ]


from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
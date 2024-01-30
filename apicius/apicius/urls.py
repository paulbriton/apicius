from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from . import views

from graphene_django.views import GraphQLView

urlpatterns = [
    path("", views.index, name="index"),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

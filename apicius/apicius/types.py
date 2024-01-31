import graphene
from graphene_django import DjangoObjectType
from apicius import models


class AuthorObjectType(DjangoObjectType):
    class Meta:
        model = models.Author


class RecipeTypeObjectType(DjangoObjectType):
    class Meta:
        model = models.RecipeType


class IngredientObjectType(DjangoObjectType):
    class Meta:
        model = models.Ingredient


class RecipeObjectType(DjangoObjectType):
    class Meta:
        model = models.Recipe

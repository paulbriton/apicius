import graphene
from apicius import models
from apicius import types


# The Query class
class Query(graphene.ObjectType):
    all_recipes = graphene.List(types.RecipeObjectType)
    all_recipe_types = graphene.List(types.RecipeTypeObjectTYpe)
    all_ingredients = graphene.List(types.IngredientObjectType)

    def resolve_all_recipes(root, info):
        return models.Recipe.objects.all()

    def resolve_all_recipe_types(root, info):
        return models.RecipeType.objects.all()

    def resolse_all_ingredients(root, info):
        return models.Ingredient.objects.all()

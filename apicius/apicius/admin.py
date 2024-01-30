from django.contrib import admin
from modeltranslation.admin import (
    TranslationAdmin,
    TranslationTabularInline,
    TabbedTranslationAdmin,
)
from .models import Recipe, Ingredient, Step, RecipeType, CookingTime, Author


class StepInline(TranslationTabularInline):
    model = Step


class RecipeIngredientInline(TranslationTabularInline):
    model = Recipe.ingredients.through
    extra = 1


class RecipeCookingTimeInline(admin.TabularInline):
    model = Recipe.cooking_times.through
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(TabbedTranslationAdmin):
    # group_fieldsets = True
    inlines = [
        RecipeIngredientInline,
        StepInline,
        RecipeCookingTimeInline,
    ]


@admin.register(Ingredient)
class IngredientAdmin(TabbedTranslationAdmin):
    pass


@admin.register(RecipeType)
class RecipeTypeAdmin(TabbedTranslationAdmin):
    pass


@admin.register(CookingTime)
class CookingTimeAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

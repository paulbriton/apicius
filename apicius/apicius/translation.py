from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Base,
    RecipeType,
    Ingredient,
    CookingTime,
    Recipe,
    RecipeIngredient,
    Step,
    UserReview,
)


class BaseTranslationOption(TranslationOptions):
    fields = ("slug",)
    required_languages = ()


class NameTranslationOptions(TranslationOptions):
    fields = ("name",)


class RecipeTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "serving_unit",
        "note",
    )


class RecipeIngredientTranslationOptions(TranslationOptions):
    fields = (
        "unit",
        "description",
    )


class StepTranslationOptions(TranslationOptions):
    fields = ("description",)


class UserReviewTranslationOptions(TranslationOptions):
    fields = ("comment",)


translator.register(Base, BaseTranslationOption)
translator.register(RecipeType, NameTranslationOptions)
translator.register(Ingredient, NameTranslationOptions)
translator.register(CookingTime, NameTranslationOptions)
translator.register(Recipe, RecipeTranslationOptions)
translator.register(RecipeIngredient, RecipeIngredientTranslationOptions)
translator.register(Step, StepTranslationOptions)
translator.register(UserReview, UserReviewTranslationOptions)

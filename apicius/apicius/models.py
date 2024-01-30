from authuser.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class RecipeType(models.Model):
    name = models.CharField(_("name"), max_length=64)

    class Meta:
        verbose_name = _("recipe_type")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(_("name"), max_length=255)

    class Meta:
        verbose_name = _("ingredient")

    def __str__(self):
        return self.name


class CookingTime(models.Model):
    name = models.CharField(_("name"), max_length=64)

    class Meta:
        verbose_name = _("cooking_time")
        verbose_name_plural = _("cooking_times")

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(_("title"), max_length=255)
    serving = models.PositiveIntegerField(_("serving"))
    serving_unit = models.CharField(_("serving_unit"), max_length=64)
    is_private = models.BooleanField(_("is_private"))
    note = models.TextField(_("note"), blank=True)

    recipe_type = models.ForeignKey(
        RecipeType, on_delete=models.RESTRICT, verbose_name=_("recipe_type")
    )
    author = models.ForeignKey(
        "Author",
        null=True,
        related_name="author_recipes",
        on_delete=models.SET_NULL,
        verbose_name=_("author"),
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through="RecipeIngredient",
        related_name="recipes",
        verbose_name=_("ingredients"),
    )
    cooking_times = models.ManyToManyField(
        CookingTime, through="RecipeCookingTime", verbose_name=_("cooking_times")
    )

    class Meta:
        verbose_name = _("recipe")

    def __str__(self):
        return self.title


class Author(User):
    favorite_recipes = models.ManyToManyField(
        Recipe, blank=True, related_name="user_favorites", verbose_name=_("favorites")
    )

    class Meta:
        verbose_name = _("author")


class RecipeIngredient(models.Model):
    unit = models.CharField(_("unit"), blank=True, max_length=64)
    description = models.TextField(_("description"), blank=True)
    quantity = models.PositiveIntegerField(_("quantity"))

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = _("recipe_ingredient")


class RecipeCookingTime(models.Model):
    minute = models.PositiveIntegerField(_("minute"))
    hour = models.PositiveIntegerField(_("hour"))

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name=_("recipe")
    )
    cooking_time = models.ForeignKey(
        CookingTime, on_delete=models.RESTRICT, verbose_name=_("cooking_time")
    )

    class Meta:
        verbose_name = _("recipe_cooking_time")

    def __str__(self):
        return f"{self.hour}:{self.minute}"


class Step(models.Model):
    description = models.TextField(_("description"))
    order = models.PositiveIntegerField(_("order"))

    recipe = models.ForeignKey(
        Recipe, related_name="steps", on_delete=models.CASCADE, verbose_name=_("recipe")
    )

    class Meta:
        verbose_name = _("step")

    def __str__(self):
        return f"{self.order}"


class UserReview(models.Model):
    rating = models.PositiveIntegerField(_("rating"))
    comment = models.TextField(_("comment"))

    recipe = models.ForeignKey(Recipe, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _("user_review")

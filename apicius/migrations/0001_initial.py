# Generated by Django 4.2.3 on 2023-07-11 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CookingTime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, verbose_name="name")),
                (
                    "name_fr",
                    models.CharField(max_length=64, null=True, verbose_name="name"),
                ),
                (
                    "name_en",
                    models.CharField(max_length=64, null=True, verbose_name="name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "name_fr",
                    models.CharField(max_length=255, null=True, verbose_name="name"),
                ),
                (
                    "name_en",
                    models.CharField(max_length=255, null=True, verbose_name="name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "title_fr",
                    models.CharField(max_length=255, null=True, verbose_name="title"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=255, null=True, verbose_name="title"),
                ),
                ("serving", models.PositiveIntegerField(verbose_name="serving")),
                (
                    "serving_unit",
                    models.CharField(max_length=64, verbose_name="serving_unit"),
                ),
                (
                    "serving_unit_fr",
                    models.CharField(
                        max_length=64, null=True, verbose_name="serving_unit"
                    ),
                ),
                (
                    "serving_unit_en",
                    models.CharField(
                        max_length=64, null=True, verbose_name="serving_unit"
                    ),
                ),
                ("is_private", models.BooleanField(verbose_name="is_private")),
                ("note", models.TextField(blank=True, verbose_name="note")),
                (
                    "note_fr",
                    models.TextField(blank=True, null=True, verbose_name="note"),
                ),
                (
                    "note_en",
                    models.TextField(blank=True, null=True, verbose_name="note"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RecipeCookingTime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("minute", models.PositiveIntegerField(verbose_name="minute")),
                ("hour", models.PositiveIntegerField(verbose_name="hour")),
            ],
        ),
        migrations.CreateModel(
            name="RecipeIngredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "unit",
                    models.CharField(blank=True, max_length=64, verbose_name="unit"),
                ),
                (
                    "unit_fr",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="unit"
                    ),
                ),
                (
                    "unit_en",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="unit"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "description_fr",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "description_en",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                ("quantity", models.PositiveIntegerField(verbose_name="quantity")),
            ],
        ),
        migrations.CreateModel(
            name="RecipeType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, verbose_name="name")),
                (
                    "name_fr",
                    models.CharField(max_length=64, null=True, verbose_name="name"),
                ),
                (
                    "name_en",
                    models.CharField(max_length=64, null=True, verbose_name="name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Step",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(verbose_name="description")),
                (
                    "description_fr",
                    models.TextField(null=True, verbose_name="description"),
                ),
                (
                    "description_en",
                    models.TextField(null=True, verbose_name="description"),
                ),
                ("order", models.PositiveIntegerField(verbose_name="order")),
            ],
        ),
        migrations.CreateModel(
            name="UserReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.PositiveIntegerField(verbose_name="rating")),
                ("comment", models.TextField(verbose_name="comment")),
                ("comment_fr", models.TextField(null=True, verbose_name="comment")),
                ("comment_en", models.TextField(null=True, verbose_name="comment")),
                (
                    "recipe",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apicius.recipe",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-05 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Producer",
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
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField(blank=True)),
                (
                    "unit",
                    models.CharField(
                        choices=[
                            ("bote", "Bote"),
                            ("botella", "Botella"),
                            ("docena", "Docena"),
                            ("garrafa", "Garrafa"),
                            ("Kg", "Kg"),
                            ("paquete", "Paquete"),
                            ("litro", "Litro"),
                            ("unidad", "Unidad"),
                        ],
                        max_length=16,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "producer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lupanes.producer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeliveryNote",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "quantity",
                    models.DecimalField(
                        decimal_places=3, max_digits=6, verbose_name="Cantidad"
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lupanes.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductPrice",
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
                ("value", models.DecimalField(decimal_places=2, max_digits=5)),
                ("start_date", models.DateField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lupanes.product",
                    ),
                ),
            ],
            options={
                "unique_together": {("product", "start_date")},
            },
        ),
    ]

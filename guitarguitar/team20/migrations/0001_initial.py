# Generated by Django 4.2.6 on 2023-10-29 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("customer_id", models.IntegerField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=256)),
                ("last_name", models.CharField(max_length=256)),
                ("email", models.EmailField(max_length=256)),
                ("phone_number", models.CharField(max_length=30)),
                ("avatar", models.URLField()),
                ("address", models.JSONField()),
                ("loyalty_level", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Products",
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
                ("sku_id", models.CharField(max_length=15, unique=True)),
                ("asn", models.CharField(max_length=12)),
                ("category", models.CharField(max_length=10)),
                ("online", models.BooleanField()),
                ("item_name", models.CharField(max_length=256)),
                ("brand_name", models.CharField(max_length=256)),
                ("description", models.CharField(max_length=2000, null=True)),
                ("product_detail", models.CharField(max_length=1000, null=True)),
                ("sales_price", models.FloatField()),
                ("picture_main", models.URLField()),
                ("qty_in_stock", models.IntegerField()),
                ("qty_on_order", models.IntegerField()),
                ("colour_option", models.IntegerField()),
                ("pickup_option", models.IntegerField()),
                ("created_on", models.DateField()),
                ("body_shape", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="team20.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
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
                ("order_id", models.IntegerField()),
                ("shipping_address", models.JSONField()),
                ("products", models.JSONField()),
                ("date_created", models.DateField()),
                ("order_total", models.FloatField()),
                ("order_status", models.IntegerField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="team20.customer",
                    ),
                ),
            ],
        ),
    ]

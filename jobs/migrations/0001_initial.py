# Generated by Django 4.1.3 on 2022-12-02 00:21

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
            name="Job",
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
                ("company", models.CharField(max_length=255)),
                ("refer_scope_link", models.URLField(max_length=1023)),
                ("refer_scope_description", models.CharField(max_length=511)),
                ("refer_requirement", models.CharField(max_length=511)),
                ("applied_users", models.JSONField(blank=True, null=True)),
                ("post_date", models.DateTimeField(auto_now_add=True)),
                (
                    "recommender",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
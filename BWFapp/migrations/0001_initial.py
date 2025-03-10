# Generated by Django 5.1.6 on 2025-03-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
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
                ("name", models.CharField(max_length=100)),
                ("nationality", models.CharField(max_length=100)),
                ("nb_tournaments", models.IntegerField()),
                ("points", models.IntegerField()),
            ],
        ),
    ]

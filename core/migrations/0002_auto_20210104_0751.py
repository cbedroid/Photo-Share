# Generated by Django 3.1.4 on 2021-01-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="slug",
            field=models.SlugField(blank=True, editable=False),
        ),
    ]

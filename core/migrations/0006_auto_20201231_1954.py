# Generated by Django 3.1.4 on 2020-12-31 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201230_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
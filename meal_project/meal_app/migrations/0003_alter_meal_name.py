# Generated by Django 4.2 on 2023-04-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_app', '0002_rename_intructions_meal_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]

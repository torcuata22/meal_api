# Generated by Django 4.2 on 2023-04-27 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='intructions',
            new_name='instructions',
        ),
    ]

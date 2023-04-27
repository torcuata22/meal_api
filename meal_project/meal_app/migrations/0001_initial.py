# Generated by Django 4.2 on 2023-04-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=10, null=True)),
                ('intructions', models.TextField(blank=True, max_length=5000, null=True)),
                ('yt_link', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(default='test')),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
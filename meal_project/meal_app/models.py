from django.db import models

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True, unique=True) #unique=True ensures the field is unique and avoids dupllicates
    category = models.CharField(max_length=10, blank = True, null = True)
    instructions = models.TextField(max_length=5000, blank = True, null = True)
    yt_link = models.URLField(blank=True, null=True)
    slug = models.SlugField(default="test")
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    

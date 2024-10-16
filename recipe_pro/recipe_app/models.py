from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.CharField(max_length=10)
    image_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
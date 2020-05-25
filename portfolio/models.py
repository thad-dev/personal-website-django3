from django.db import models

# Create your models here.
# A model is like a class and can interact with db
# Changing models require a migration for db

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    tech = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
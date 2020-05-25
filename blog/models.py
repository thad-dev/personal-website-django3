from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    category = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='blog/images/', blank=True)

    def __str__(self):
        return self.title

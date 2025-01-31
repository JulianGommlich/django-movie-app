from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length = 100)
    release_year = models.IntegerField(default = 0)
    genre = models.CharField(max_length= 100)
    is_available = models.BooleanField(default = False)

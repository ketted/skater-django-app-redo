from django.db import models
import datetime

# Create your models here.

class Skater(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='skaters/img/%Y/%m/%d')
    videos = models.TextField()
    # sponsors = models.TextField()
    pro = models.BooleanField()

    def __str__(self):
        return self.name[:50]
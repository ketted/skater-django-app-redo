from django.db import models
from skaters.models import Skater


# Create your models here.
class Team(models.Model):
    brand = models.CharField(max_length=255)
    est = models.IntegerField()
    olympics = models.BooleanField()
    skaters = models.ManyToManyField(Skater, blank=True, related_name='team')
    
    def __str__(self):
        return self.brand[:50]
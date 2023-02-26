from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=100)
    gta = models.BooleanField(default=False)
    nfs = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)
    spiderman = models.BooleanField(default=False)
    uncharted = models.BooleanField(default=False)
    tombraider = models.BooleanField(default=False)
    dmc = models.BooleanField(default=False)
    sam = models.BooleanField(default=False)
    division = models.BooleanField(default=False)
    cod = models.BooleanField(default=False)

    

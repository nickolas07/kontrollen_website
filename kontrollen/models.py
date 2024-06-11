import datetime

from django.db import models


# Create your models here.
class Kontrollen(models.Model):
    name = models.CharField(max_length=100, default='')
    identifier = models.CharField(max_length=300, default='',
                                  help_text='Name, welchen die Python Dateien besitzen (ohne .py)', unique=True)
    fach = models.CharField(max_length=100, default='Mathematik')
    thema = models.CharField(max_length=150, default='', null=True, blank=True)
    jahrgang = models.IntegerField()
    sichtbar = models.BooleanField(default=True)
    beispiel = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class ErstellteKontrollen(models.Model):
    identifier = models.CharField(max_length=300, unique=False)
    datum = models.DateField(default=datetime.date.today)
    uuid = models.CharField(max_length=33, unique=True)

    def __str__(self):
        return f'{self.identifier} {self.uuid}'

    class Meta:
        ordering = ['datum']

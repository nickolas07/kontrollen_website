from django.db import models


# Create your models here.
class Themen(models.Model):
    themen_name = models.CharField(max_length=100)

    def __str__(self):
        return self.themen_name

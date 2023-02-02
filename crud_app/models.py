from django.db import models

# Create your models here.


class Hotel(models.Model):
    room = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    cdate = models.DateField()
from django.db import models

# Create your models here.

class Contributor(models.Model):
    institution = models.ForeignKey('Institution', related_name='staff')


class Institution(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

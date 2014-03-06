from django.db import models
from django.conf import settings

# Create your models here.

class Contributor(models.Model):
    institution = models.ForeignKey('Institution')
    user = models.OneToOneField(settings.AUTH_USER_MODEL)


class Institution(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

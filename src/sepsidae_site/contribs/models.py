from django.db import models

# Create your models here.

class Contributor(models.Model):
    institution = models.ForeignKey('Institution', related_name='staff')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{last_name}, {first_name}".format(last_name=self.last_name,
                                                   first_name=self.first_name)


class Institution(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{self.name} ({self.country})".format(self=self)

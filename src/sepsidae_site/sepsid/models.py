from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Species(models.Model):
    name = models.CharField(max_length=100)
    genus = models.ForeignKey('Genus')

    contributors = models.ManyToManyField('contribs.Contributor',
                                          related_name="contributions",
                                          blank=True,
                                          null=True)

    reference_paper = models.CharField(max_length=100,
                                       blank=True,
                                       null=True)

    discovered_who = models.CharField(max_length=100,
                                      null=True,
                                      blank=True)
    discovered_when = models.PositiveIntegerField(blank=True,
                                                  null=True)

    thumbnail = models.ImageField(upload_to="species/thumbnails/",
                                  null=True,
                                  blank=True)

    def clean(self):
        if not (1000 < self.discovered_when <= date.today().year) and not self.discovered_when == None:
            raise ValidationError("discovered_when Year must be a sane "
                                  "value: 1000 < {} < {}".format(
                                      self.discovered_when, date.today().year))

    def save(self, *args, **kwargs):
        self.clean()
        return super(Species, self).save(*args, **kwargs)

    def full_name(self):
        return u"{genus} {species}".format(
            species=self.name,
            genus=self.genus.name
        )

    def __unicode__(self):
        return self.full_name()


class Genus(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

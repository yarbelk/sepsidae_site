from django.db import models

class Species(models.Model):
    name = models.CharField(max_length=100)
    genus_name = models.CharField(max_length=100)


    def full_name(self):
        return u"{genus} {species}".format(
            species=self.name,
            genus=self.genus_name
        )

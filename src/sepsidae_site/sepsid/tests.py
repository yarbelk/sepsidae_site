from __future__ import unicode_literals

from rest_framework.test import APITestCase

#from contribs.factories import UserFactory, ContributorFactory

from .factories import SpeciesFactory

### Model tests

class SpeciesTestCases(APITestCase):
    def test_species_exists_with_full_name(self):
        species_with_name = SpeciesFactory.create()
        self.assertEquals(species_with_name.full_name(), "genus_name species_name")

    def test_can_specify_species_name(self):
        species_specified_name = SpeciesFactory.create(name="superfly")
        self.assertEquals(species_specified_name.full_name(), "genus_name superfly")
        self.assertEquals(species_specified_name.name, "superfly")

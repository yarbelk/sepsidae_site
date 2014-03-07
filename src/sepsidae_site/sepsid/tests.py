from __future__ import unicode_literals

from rest_framework.test import APITestCase
from rest_framework.parsers import JSONParser

from contribs.factories import ContributorFactory, InstitutionFactory

from .factories import SpeciesFactory, GenusFactory

from datetime import date
from django.core.exceptions import ValidationError

json_parser = JSONParser()

### Model tests

class SpeciesTestCases(APITestCase):
    def setUp(self):
        super(SpeciesTestCases, self).setUp()
        self.contributor_one = ContributorFactory.create()
        self.contributor_two = ContributorFactory.create()

        self.species_one_contrib = SpeciesFactory.create()
        self.species_one_contrib.contributors.add(self.contributor_one)

        self.species_two_contrib = SpeciesFactory.create()
        self.species_two_contrib.contributors.add(self.contributor_one)
        self.species_two_contrib.contributors.add(self.contributor_two)

    def test_species_exists_with_full_name(self):
        species_with_name = SpeciesFactory.create()
        self.assertEquals(species_with_name.full_name(), "genus_name species_name")

    def test_can_specify_species_name(self):
        species_specified_name = SpeciesFactory.create(name="superfly")
        self.assertEquals(species_specified_name.full_name(), "genus_name superfly")
        self.assertEquals(species_specified_name.name, "superfly")

    def test_species_requires_genus(self):
        with self.assertRaises(ValueError):
            SpeciesFactory.create(genus=None)

    def test_species_has_contributors(self):
        self.assertEquals(self.species_one_contrib.contributors.all().count(), 1)
        self.assertIn(self.contributor_one,
                      self.species_one_contrib.contributors.all())

        self.assertEquals(self.species_two_contrib.contributors.all().count(), 2)
        self.assertIn(self.contributor_one,
                      self.species_two_contrib.contributors.all())
        self.assertIn(self.contributor_two,
                      self.species_two_contrib.contributors.all())

    def test_can_get_species_by_contributor(self):
        self.assertEquals(self.contributor_one.contributions.all().count(), 2)
        self.assertIn(self.species_one_contrib,
                      self.contributor_one.contributions.all())
        self.assertIn(self.species_two_contrib,
                      self.contributor_one.contributions.all())

        self.assertNotIn(self.species_one_contrib,
                         self.contributor_two.contributions.all())

    def test_species_has_reference_paper(self):
        self.assertEquals(
            self.species_one_contrib.reference_paper,
            u"Ozerov, 2005")

    def test_species_can_have_discovered_who_date(self):
        self.assertIsNone(self.species_one_contrib.discovered_who)
        self.assertIsNone(self.species_one_contrib.discovered_when)

        species_discovered = SpeciesFactory(discovered_who="John",
                                            discovered_when=2005)
        self.assertEquals(species_discovered.discovered_who, "John")
        self.assertEquals(species_discovered.discovered_when, 2005)

    def test_species_discovered_when_sane(self):
        with self.assertRaises(ValidationError):
            no_negative_year = SpeciesFactory.create(discovered_when=-100)
        with self.assertRaises(ValidationError):
            today = date.today()
            no_future_year = SpeciesFactory.create(discovered_when=today.year+1)
        with self.assertRaises(ValidationError):
            no_early_years= SpeciesFactory.create(discovered_when=1000)

    def test_species_has_image(self):
        imaged_fly = SpeciesFactory.create()
        self.assertIsNotNone(imaged_fly.thumbnail)



class GenusTestCases(APITestCase):
    def test_genus_exists_with_name(self):
        named_genus = GenusFactory.create()

        self.assertIsNotNone(named_genus.id)
        self.assertEquals(named_genus.name, 'genus_name')

    def test_can_specify_genus_name(self):
        named_genus = GenusFactory.create(name='Sepsid')
        self.assertIsNotNone(named_genus.id)
        self.assertEquals(named_genus.name, 'Sepsid')

    def test_can_list_all_member_species(self):
        parent_genus = GenusFactory.create(name="parent")
        child_one = SpeciesFactory.create(
            name="child_one",
            genus=parent_genus
        )
        child_two = SpeciesFactory.create(
            name="child_two",
            genus=parent_genus
        )

        children = parent_genus.species_set.all()

        self.assertEquals(children.count(), 2)
        self.assertIn(child_one, children)
        self.assertIn(child_two, children)

import factory

from django.contrib.auth import get_user_model

User = get_user_model()

class GenusFactory(factory.DjangoModelFactory):
    FACTORY_FOR = 'sepsid.Genus'

    name = 'genus_name'

class SpeciesFactory(factory.DjangoModelFactory):
    FACTORY_FOR = 'sepsid.Species'

    name = 'species_name'
    genus = factory.SubFactory(GenusFactory)
    reference_paper = u"Ozerov, 2005"

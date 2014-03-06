import factory

from django.contrib.auth import get_user_model

User = get_user_model()

class SpeciesFactory(factory.DjangoModelFactory):
    FACTORY_FOR = 'sepsid.Species'

    name = 'species_name'
    genus_name = 'genus_name'

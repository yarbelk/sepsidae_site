import factory

from django.contrib.auth import get_user_model

User = get_user_model()


class InstitutionFactory(factory.DjangoModelFactory):
    FACTORY_FOR = 'contribs.Institution'

    name = 'NUS'
    country = 'Singapore'

class ContributorFactory(factory.DjangoModelFactory):
    FACTORY_FOR = 'contribs.Contributor'

    institution = factory.SubFactory(InstitutionFactory)

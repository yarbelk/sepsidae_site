import factory

from .models import Contributor

from django.contrib.auth import get_user_model

User = get_user_model()

class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User

    username = factory.sequence(lambda x: 'user {}'.format(x))
    first_name = 'First Name'
    last_name = 'Last Name'


class InstitutionFactory(factory.DjangoModelFactory):
    FACTORY_FOR = 'contribs.Institution'

    name = 'NUS'
    country = 'Singapore'

class ContributorFactory(factory.DjangoModelFactory):
    FACTORY_FOR = 'contribs.Contributor'

    user = factory.SubFactory(UserFactory)
    institution = factory.SubFactory(InstitutionFactory)

from __future__ import unicode_literals

from rest_framework.test import APIRequestFactory, APITestCase

from .factories import UserFactory, ContributorFactory, InstitutionFactory

# Create your tests here.

### Model tests

class UserTestCases(APITestCase):
    def test_can_create_user(self):
        user = UserFactory.create()
        self.assertIsNotNone(user.id)

    def test_user_has_name_email(self):
        user = UserFactory.create(
            first_name='Jim',
            last_name='Bob',
            email='jim@bob.com'
        )
        self.assertEquals(user.first_name, 'Jim')
        self.assertEquals(user.last_name, 'Bob')
        self.assertEquals(user.email, 'jim@bob.com')

    def test_user_has_contributor(self):
        user = UserFactory.create()
        contributor = ContributorFactory.create(user=user)
        self.assertIsNotNone(contributor.id)

    def test_contributor_has_institution(self):
        contributor = ContributorFactory.create()

        self.assertIsNotNone(contributor.institution)

    def test_institute_has_name_country(self):
        institution = InstitutionFactory.create(
            name="NUS",
            country="Singapore"
        )
        self.assertIsNotNone(institution.id)
        self.assertEquals(institution.name, "NUS")
        self.assertEquals(institution.country, "Singapore")

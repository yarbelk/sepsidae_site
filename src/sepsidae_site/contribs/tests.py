from __future__ import unicode_literals

from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .factories import ContributorFactory, InstitutionFactory

json_parser = JSONParser()

### Model tests

class ContribInstituteTestCases(APITestCase):
    def test_contributor_has_institution(self):
        contributor = ContributorFactory.create()

        self.assertIsNotNone(contributor.institution)

    def test_contributor_has_name(self):
        named_contrib = ContributorFactory.create(
            first_name='Jim',
            last_name='Bob'
        )
        self.assertEquals(named_contrib.first_name, 'Jim')
        self.assertEquals(named_contrib.last_name, 'Bob')


    def test_institute_has_name_country(self):
        institution = InstitutionFactory.create(
            name="NUS",
            country="Singapore"
        )
        self.assertIsNotNone(institution.id)
        self.assertEquals(institution.name, "NUS")
        self.assertEquals(institution.country, "Singapore")

## Viewset Tests

class InstitutionViewsetTest(APITestCase):
    def setUp(self):
        super(InstitutionViewsetTest, self).setUp()
        self.institution_with_noone = InstitutionFactory.create()
        self.institution_one = InstitutionFactory.create(name="SUTD")
        self.contrib_one = ContributorFactory.create(institution=self.institution_one)

    def login(self, user, password=None, oauth=False):
        return self.client.login(username=user.username, password=password)

    def test_there_is_a_list_of_institutes(self):
        institute_list_uri = reverse("institution-list")
        list_response = self.client.get(institute_list_uri)
        self.assertEquals(len(list_response.data),2)


class ContributorViewsetTest(APITestCase):
    def setUp(self):
        super(ContributorViewsetTest, self).setUp()
        self.contrib_one = ContributorFactory.create()
        self.contrib_two  = ContributorFactory.create()

    def login(self, user, password=None, oauth=False):
        return self.client.login(username=user.username, password=password)

    def test_there_is_a_list_of_contributors(self):
        contrib_list_uri = reverse("contributor-list")
        response = self.client.get(contrib_list_uri)

    def test_contributors_have_details(self):
        detail_uri = reverse('contributor-detail', kwargs={'pk':self.contrib_one.id})

        response = self.client.get(detail_uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('url',response.data)
        self.assertIn('first_name',response.data)
        self.assertIn('last_name',response.data)
        self.assertIn('institution',response.data)

    def test_cannot_do_unsafe_things_to_contributors(self):
        contrib_list_uri = reverse("contributor-list")
        contrib_detail_uri = reverse('contributor-detail', kwargs={'pk':self.contrib_one.id})

        post_fail_response = self.client.post(
            contrib_list_uri,
            data={
                    "first_name": "john",
                    "last_name": "smith",
                    "institution_uri": {
                        "name": "NUS",
                        "country": "Singapore"}})
        self.assertEquals(post_fail_response.status_code, 403)

        patch_fail_response = self.client.patch(
            contrib_detail_uri,
            data={
                    "first_name": "john",
                    "last_name": "smith",
                    "institution_uri": {
                        "name": "NUS",
                        "country": "Singapore"}})
        self.assertEquals(patch_fail_response.status_code, 403)

        delete_fail_response = self.client.delete(contrib_detail_uri)
        self.assertEquals(delete_fail_response.status_code, 403)

from rest_framework import serializers

from .models import Institution, Contributor


class ContributorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contributor
        fields = ['url', 'first_name', 'last_name', 'institution']


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    staff = serializers.RelatedField(many=True)

    class Meta:
        model = Institution
        fiels = ['url', 'name', 'country', 'staff']

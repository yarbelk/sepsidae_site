from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Institution, Contributor

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ContributorSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(max_length=100, source="user.first_name")
    last_name = serializers.CharField(max_length=100, source="user.last_name")

    class Meta:
        model = Contributor
        fields = ['url', 'first_name', 'last_name', 'institution']


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    staff = serializers.RelatedField(many=True)

    class Meta:
        model = Institution
        fiels = ['url', 'name', 'country', 'staff']

from rest_framework import serializers

from .models import Species, Genus


class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.CharField(source="full_name")

    class Meta:
        model = Species

class GenusSerializer(serializers.HyperlinkedModelSerializer):
    #full_name = serializers.CharField(source="full_name")

    class Meta:
        model = Genus

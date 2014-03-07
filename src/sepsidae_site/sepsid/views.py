from rest_framework import viewsets

from .models import Species, Genus
from .serializers import SpeciesSerializer, GenusSerializer


class SpeciesViewset(viewsets.ReadOnlyModelViewSet):
    model = Species
    serializer_class = SpeciesSerializer

class GenusViewset(viewsets.ReadOnlyModelViewSet):
    model = Genus
    serializer_class = GenusSerializer

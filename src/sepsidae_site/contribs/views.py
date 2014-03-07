from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import (viewsets, status)

from .models import Contributor, Institution
from .serializers import ContributorSerializer, InstitutionSerializer

class ContributorViewSet(viewsets.ReadOnlyModelViewSet):
    model = Contributor
    serializer_class = ContributorSerializer

class InstitutionViewSet(viewsets.ReadOnlyModelViewSet):
    model = Institution
    serializer_class = InstitutionSerializer

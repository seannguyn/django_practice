from django.shortcuts import render
from rest_framework import viewsets
from languages.models import Language
from languages.serializers import LanguageSerialzer

# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerialzer

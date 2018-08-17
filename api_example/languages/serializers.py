from rest_framework import serializers
from languages.models import Language

class LanguageSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id','name','paradigm')

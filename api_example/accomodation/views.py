from django.shortcuts import render
from rest_framework import viewsets
from accomodation.models import Accomodation, HouseApartmentVilla, RoomStudio
from accomodation.serializers import AccommodationSerializer, HouseApartmentVillaSerializer, RoomStudioSerializer

# Create your views here.

class AccommodationView(viewsets.ModelViewSet):
    queryset = Accomodation.objects.all()
    # queryset = Accomodation.objects.filter(user__username__exact="sean")
    serializer_class = AccommodationSerializer

class HouseApartmentVillaView(viewsets.ModelViewSet):
    queryset = HouseApartmentVilla.objects.all()
    serializer_class = HouseApartmentVillaSerializer

class RoomStudioView(viewsets.ModelViewSet):
    queryset = RoomStudio.objects.all()
    serializer_class = RoomStudioSerializer

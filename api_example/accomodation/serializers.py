from rest_framework import serializers
from accomodation.models import Accomodation, HouseApartmentVilla, RoomStudio

class AccommodationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accomodation
        fields = ('id','user','Accomodation_Type','area','floors','bedroom_master','bedroom',
                    'kitchen','bathroom','pool',
                    'laundry','gym','entertainment','carpark','description')

class HouseApartmentVillaSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseApartmentVilla
        fields = ('accommodation','area','floors','bedroom_master','bedroom',
                    'kitchen','bathroom','pool',
                    'laundry','gym','entertainment','carpark','description')

class RoomStudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomStudio
        fields = ('accommodation','area','bedroom',
                    'kitchen','bathroom','description')

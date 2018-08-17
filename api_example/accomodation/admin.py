from django.contrib import admin
from accomodation.models import Accomodation, UserInfo, HouseApartmentVilla, RoomStudio
# Register your models here.

admin.site.register(Accomodation)
admin.site.register(UserInfo)
admin.site.register(HouseApartmentVilla)
admin.site.register(RoomStudio)

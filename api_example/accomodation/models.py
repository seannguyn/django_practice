from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pic", blank=True)


class Accomodation(models.Model):

    ACCOMMODATION_TYPES = (
        ('Room', 'Room'),
        ('Studio', 'Studio'),
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Villa', 'Villa'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    Accomodation_Type = models.CharField(max_length=10, choices=ACCOMMODATION_TYPES)

    area            = models.IntegerField(default=1, blank=False)
    floors          = models.IntegerField(default=1, blank=False)
    bedroom_master  = models.IntegerField(default=1, blank=False)
    bedroom         = models.IntegerField(default=1, blank=False)
    kitchen         = models.IntegerField(default=1, blank=False)
    bathroom        = models.IntegerField(default=1, blank=False)

    pool            = models.IntegerField(default=0, blank=False)
    laundry         = models.IntegerField(default=0, blank=False)
    gym             = models.IntegerField(default=0, blank=False)
    entertainment   = models.IntegerField(default=0, blank=False)
    carpark         = models.IntegerField(default=0, blank=False)

    description     = models.TextField(blank=True)

    def __str__(self):
        return self.user.username + "_"+self.Accomodation_Type+"_" + str(self.id);

class HouseApartmentVilla(models.Model):

    accommodation   = models.OneToOneField(Accomodation,on_delete=models.CASCADE,primary_key=True)

    area            = models.IntegerField(default=1, blank=False)
    floors          = models.IntegerField(default=1, blank=False)
    bedroom_master  = models.IntegerField(default=1, blank=False)
    bedroom         = models.IntegerField(default=1, blank=False)
    kitchen         = models.IntegerField(default=1, blank=False)
    bathroom        = models.IntegerField(default=1, blank=False)

    pool            = models.IntegerField(default=0, blank=False)
    laundry         = models.IntegerField(default=0, blank=False)
    gym             = models.IntegerField(default=0, blank=False)
    entertainment   = models.IntegerField(default=0, blank=False)
    carpark         = models.IntegerField(default=0, blank=False)

    description     = models.TextField(blank=True)

class RoomStudio(models.Model):

    accommodation   = models.OneToOneField(Accomodation,on_delete=models.CASCADE,primary_key=True)

    area            = models.IntegerField(default=1, blank=False)
    bedroom         = models.IntegerField(default=1, blank=False)
    kitchen         = models.IntegerField(default=1, blank=False)
    bathroom        = models.IntegerField(default=1, blank=False)

    description     = models.TextField(blank=True)

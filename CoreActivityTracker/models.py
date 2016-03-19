from __future__ import unicode_literals

from django.db import models


class SpokenLanguage(models.Model):
    english_name = models.CharField(max_length=50)
    iso_639_2_code = models.CharField(max_length=3)
    iso_639_1_code = models.CharField(max_length=2)
    biblio_or_term = models.CharField(max_length=1)


class DeclarationStatus(models.Model):
    BAHAI = 'BA'
    FRIEND_OF_FAITH = 'FO'
    DONT_KNOW = 'DO'
    SPECTATOR = 'SP'
    DECLARATION_STATUS_CHOICES = (
        (BAHAI, 'Baha\'i'),
        (FRIEND_OF_FAITH, 'Friend of Faith'),
        (DONT_KNOW, 'Don\'t know'),
        (SPECTATOR, 'Spectator'),
    )
    declaration_status = models.CharField(
        max_length=2,
        choices=DECLARATION_STATUS_CHOICES,
        default=DONT_KNOW
    )


class DeclarationStatusName(models.Model):
    language = models.ForeignKey(
        SpokenLanguage,
        on_delete=models.CASCADE
    )
    declaration_status = models.ForeignKey(
        DeclarationStatus,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=35)


class Person(models.Model):
    first_name = models.CharField(max_length=35)
    last_name  = models.CharField(max_length=35)
    declaration_status_name = models.ForeignKey(
        DeclarationStatusName
    )


class ActivityType(models.Model):
    DEVOTIONAL = 'DV'
    STUDY_CIRCLE = 'SC'
    ACTIVITY_TYPE_CHOICES = (
        (DEVOTIONAL, 'Devotional'),
        (STUDY_CIRCLE, 'Study Cicle'),
    )
    activity_type = models.CharField(
        max_length=2,
        choices=ACTIVITY_TYPE_CHOICES,
    )
    

class ActivityTypeName(models.Model):
    language = models.ForeignKey(
        SpokenLanguage,
        on_delete=models.CASCADE
    )
    activity_type = models.ForeignKey(
        ActivityType,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=35)


class Country(models.Model):
    name = models.CharField(max_length=35)
    code = models.CharField(max_length=3)
    iso_2 = models.CharField(max_length=2)
    iso_3 = models.CharField(max_length=3)
    
    
class Location(models.Model):
    label = models.CharField(max_length=35)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_or_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=35)
    country = models.ForeignKey(Country)
    latitude_degrees = models.FloatField()
    longitude_degrees = models.FloatField()
    
    
class ActivityReport(models.Model):
    persons = models.ManyToManyField(Person)
    activity_type = models.ForeignKey(
        ActivityTypeName
    )
    location = models.ForeignKey(
        Location
    )
    
    
# ActivityReport:
# DONE reference to a UserHistory
# DONE type (e.g. devotional, study circle, etc, including non-core activites as well)
# reference to Location
# date/time occurrence
# date/time reported
# 
# Location
# label
# address 1
# address 1
# city
# state/province
# postal code
# country
# latitude
# longitude

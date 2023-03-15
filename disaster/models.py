from django.db import models


class Disaster(models.Model):
    disasterNo = models.TextField(primary_key=True)
    year = models.IntegerField()
    seq = models.IntegerField()
    group = models.TextField()
    subgroup = models.TextField()
    Type = models.TextField()
    subtype = models.TextField(null=True)
    eventName = models.TextField(null=True)
    country = models.TextField()
    iso = models.TextField()
    region = models.TextField()
    continent = models.TextField()
    location = models.TextField()
    startYear = models.IntegerField(null=True)
    startMonth = models.IntegerField(null=True)
    startDay = models.IntegerField(null=True)
    endYear = models.IntegerField(null=True)
    endMonth = models.IntegerField(null=True)
    endDay = models.IntegerField(null=True)
    totalDeaths = models.IntegerField(null=True)
    injured = models.IntegerField(null=True)
    affected = models.IntegerField(null=True)
    totalAffected = models.IntegerField(null=True)
    homeless = models.IntegerField(null=True)
    damageCost = models.IntegerField(null=True)


class Continent(models.Model):
    id = models.TextField(primary_key=True)


class Region(models.Model):
    id = models.TextField(primary_key=True)
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE)

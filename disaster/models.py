from django.db import models


class Disaster(models.Model):
    disasterNo = models.TextField(primary_key=True)
    year = models.IntegerField()
    seq = models.IntegerField()
    group = models.TextField()
    subgroup = models.TextField()
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    subtype = models.TextField(null=True, blank=True)
    eventName = models.TextField(null=True, blank=True)
    country = models.TextField()
    iso = models.TextField()
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE)
    location = models.TextField()
    startYear = models.IntegerField(null=True, blank=True)
    startMonth = models.IntegerField(null=True, blank=True)
    startDay = models.IntegerField(null=True, blank=True)
    endYear = models.IntegerField(null=True, blank=True)
    endMonth = models.IntegerField(null=True, blank=True)
    endDay = models.IntegerField(null=True, blank=True)
    totalDeaths = models.IntegerField(null=True, blank=True)
    injured = models.IntegerField(null=True, blank=True)
    affected = models.IntegerField(null=True, blank=True)
    totalAffected = models.IntegerField(null=True, blank=True)
    homeless = models.IntegerField(null=True, blank=True)
    damageCost = models.IntegerField(null=True, blank=True)


class Continent(models.Model):
    id = models.TextField(primary_key=True)

    def __str__(self):
        return self.id


class Region(models.Model):
    id = models.TextField(primary_key=True)
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Type(models.Model):
    id = models.TextField(primary_key=True)

    def __str__(self):
        return self.id

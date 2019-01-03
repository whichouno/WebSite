from django.db import models

class ChinaCities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    province = models.ForeignKey('ChinaProvinces', models.DO_NOTHING, blank=True, null=True)
    citycode = models.CharField(max_length=100, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    mergername = models.CharField(max_length=100, blank=True, null=True)
    beento = models.IntegerField()

    class Meta:
        app_label = 'BeenTo'
        managed = False
        db_table = 'china_cities'

class ChinaProvinces(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)
    pinyin = models.CharField(max_length=100, blank=True, null=True)
    district_type = models.ForeignKey('DistrictType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        app_label = 'BeenTo'
        managed = False
        db_table = 'china_provinces'

class DistrictType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'BeenTo'
        managed = False
        db_table = 'district_type'
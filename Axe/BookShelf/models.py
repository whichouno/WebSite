from django.db import models

class Continents(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'BookShelf'
        managed = False
        db_table = 'continents'

class States(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    continent = models.ForeignKey(Continents,on_delete=models.DO_NOTHING)

    class Meta:
        app_label = 'BookShelf'
        managed = False
        db_table = 'states'

class Authors(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    birth = models.IntegerField(blank=True, null=True)
    death = models.IntegerField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    state = models.ForeignKey('States', models.DO_NOTHING)

    class Meta:
        app_label = 'BookShelf'
        managed = False
        db_table = 'authors'

class BookStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(unique=True, max_length=20, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        app_label = 'BookShelf'
        managed = False
        db_table = 'book_status'

class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(Authors, models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey(BookStatus, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        app_label = 'BookShelf'
        managed = False
        db_table = 'books'
        unique_together = (('name', 'author'),)



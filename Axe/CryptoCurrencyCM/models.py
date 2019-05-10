from django.db import models

class Bitcoin(models.Model):
    date = models.DateField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'CryptoCurrencyCM'
        managed = False
        db_table = 'Bitcoin'

class Ethereumclassic(models.Model):
    date = models.DateField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'CryptoCurrencyCM'
        managed = False
        db_table = 'EthereumClassic'

class Ethereum(models.Model):
    date = models.DateField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'CryptoCurrencyCM'
        managed = False
        db_table = 'Ethereum'

class Bitcoincash(models.Model):
    date = models.DateField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'CryptoCurrencyCM'
        managed = False
        db_table = 'BitcoinCash'

class Litecoin(models.Model):
    date = models.DateField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Litecoin'

class Neo(models.Model):
    date = models.DateField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NEO'

class Eos(models.Model):
    date = models.DateField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EOS'

class Bitshares(models.Model):
    date = models.DateField(primary_key=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BitShares'



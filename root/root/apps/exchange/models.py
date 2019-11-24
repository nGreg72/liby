# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SpZakup(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.IntegerField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    rate = models.IntegerField()
    inform = models.TextField()
    level = models.IntegerField()
    cat = models.IntegerField()
    proc = models.IntegerField()
    min = models.IntegerField()
    mintype = models.IntegerField(db_column='minType')  # Field name made lowercase.
    curs = models.FloatField()
    bonus = models.IntegerField()
    dost = models.IntegerField()
    status = models.IntegerField()
    foto = models.CharField(max_length=255)
    alertnews = models.IntegerField()
    alertcomm = models.IntegerField()
    comment = models.IntegerField()
    id_check = models.IntegerField()
    russia = models.CharField(max_length=100)
    date = models.IntegerField()
    rekviz = models.TextField()
    type = models.IntegerField()
    file1 = models.CharField(max_length=255)
    file2 = models.CharField(max_length=255)
    file3 = models.CharField(max_length=255)
    price_name1 = models.CharField(max_length=100, blank=True, null=True)
    price_name2 = models.CharField(max_length=100, blank=True, null=True)
    price_name3 = models.CharField(max_length=100, blank=True, null=True)
    office = models.TextField()
    paytype = models.IntegerField()
    hot = models.IntegerField()
    top = models.IntegerField()
    soonstop = models.IntegerField(db_column='soonStop')  # Field name made lowercase.
    datestop = models.CharField(db_column='dateStop', max_length=50)  # Field name made lowercase.
    owner_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_zakup'

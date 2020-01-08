# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    podcat = models.IntegerField()
    name = models.CharField(max_length=255)
    cat_chpu = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'


class Cities(models.Model):
    id_city = models.AutoField(primary_key=True)
    id_region = models.PositiveIntegerField()
    id_country = models.PositiveIntegerField()
    city_name_ru = models.CharField(max_length=255, blank=True, null=True)
    city_name_en = models.CharField(max_length=255)
    city_order = models.PositiveIntegerField()
    show = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cities'


class Countries(models.Model):
    id_country = models.AutoField(primary_key=True)
    country_name_ru = models.CharField(max_length=50, blank=True, null=True)
    country_name_en = models.CharField(max_length=50)
    country_iso = models.CharField(max_length=2, blank=True, null=True)
    country_order = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'countries'


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    fgid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group'


class Message(models.Model):
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.IntegerField()
    date = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    view = models.IntegerField()
    tresh = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message'


class MessageContacts(models.Model):
    user = models.IntegerField()
    contact = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_contacts'


class News(models.Model):
    user = models.IntegerField()
    cat = models.IntegerField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    rate = models.IntegerField()
    chpu = models.CharField(max_length=255)
    date = models.CharField(max_length=20)
    show_date = models.IntegerField()
    view = models.IntegerField()
    tags_ru = models.TextField()
    tags_en = models.TextField()
    original_url = models.CharField(max_length=255)
    thumbs = models.CharField(max_length=255)
    comments = models.IntegerField()
    moderate = models.IntegerField()
    group = models.TextField()

    class Meta:
        managed = False
        db_table = 'news'


class Office(models.Model):
    id = models.AutoField(primary_key=True)
    podcat = models.IntegerField()
    name = models.CharField(max_length=255)
    cat_chpu = models.CharField(max_length=255)
    thumbs = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'office'


class OfficeSet(models.Model):
    user = models.IntegerField()
    zp_id = models.IntegerField()
    office = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'office_set'


class PunbbUsers(models.Model):
    group_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=80)
    realname = models.CharField(max_length=40, blank=True, null=True)
    no_answer = models.IntegerField(blank=True, null=True)
    registered = models.PositiveIntegerField()
    registration_ip = models.CharField(max_length=39)
    last_visit = models.PositiveIntegerField()
    city = models.PositiveIntegerField()
    region = models.PositiveIntegerField()
    country = models.PositiveIntegerField()
    phone = models.CharField(max_length=255)
    wm = models.FloatField()
    display_name = models.CharField(max_length=100)
    user_url = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'punbb_users'


class Regions(models.Model):
    id_region = models.AutoField(primary_key=True)
    id_country = models.PositiveIntegerField()
    region_name_ru = models.CharField(max_length=255, blank=True, null=True)
    region_name_en = models.CharField(max_length=255)
    region_order = models.PositiveIntegerField()
    show = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'regions'


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'session'


class Setting(models.Model):
    name = models.CharField(max_length=50)
    desk = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'setting'


class SpAddOrg(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.IntegerField()
    status = models.IntegerField()
    region = models.IntegerField()
    city = models.IntegerField()
    country = models.IntegerField()
    opyt = models.IntegerField()
    post = models.IntegerField()
    site = models.TextField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    activate = models.IntegerField()
    pass_field = models.CharField(db_column='pass', max_length=255)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'sp_add_org'


class SpAddpay(models.Model):
    zp_id = models.IntegerField()
    user = models.IntegerField()
    date = models.IntegerField()
    date_user = models.CharField(max_length=255)
    summ = models.FloatField()
    summextra = models.FloatField(db_column='summExtra')  # Field name made lowercase.
    card = models.CharField(max_length=255)
    status = models.IntegerField()
    doplata = models.FloatField()
    fldop = models.IntegerField()
    transp = models.FloatField()
    transpuser = models.FloatField(db_column='transpUser')  # Field name made lowercase.
    transpstatus = models.IntegerField(db_column='transpStatus')  # Field name made lowercase.
    bankname = models.CharField(db_column='bankName', max_length=10)  # Field name made lowercase.
    whopay = models.CharField(db_column='whoPay', max_length=50)  # Field name made lowercase.
    banknametransp = models.IntegerField(db_column='bankNameTransp')  # Field name made lowercase.
    whopaytransp = models.CharField(db_column='whoPayTransp', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sp_addpay'


class SpAddpayorg(models.Model):
    zp_id = models.IntegerField()
    user = models.IntegerField()
    date = models.IntegerField()
    date_user = models.CharField(max_length=255)
    summ = models.FloatField()
    card = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_addpayorg'


class SpCat(models.Model):
    podcat = models.IntegerField()
    name = models.CharField(max_length=255)
    cat_chpu = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sp_cat'


class SpCatSub(models.Model):
    id = models.AutoField(primary_key=True)
    zakup = models.IntegerField()
    cat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_cat_sub'


class SpDelivery(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sp_delivery'


class SpLevel(models.Model):
    name = models.CharField(max_length=255)
    discr = models.TextField()

    class Meta:
        managed = False
        db_table = 'sp_level'


class SpOrder(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.IntegerField()
    id_order = models.CharField(max_length=255)
    message = models.TextField()
    mess_edit = models.TextField()
    color = models.CharField(max_length=255)
    kolvo = models.IntegerField()
    oversize = models.FloatField()
    date = models.CharField(max_length=20)
    uniqcod = models.CharField(max_length=20)
    id_zp = models.IntegerField()
    id_ryad = models.IntegerField()
    dateunix = models.IntegerField()
    status = models.IntegerField()
    addrdelivery = models.IntegerField(db_column='addrDelivery')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sp_order'


class SpOrgorder(models.Model):
    date = models.IntegerField()
    sum = models.FloatField()
    zp_id = models.IntegerField()
    user = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_orgorder'


class SpPristroy(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.IntegerField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    cat = models.IntegerField()
    date = models.IntegerField()
    price = models.IntegerField()
    size = models.CharField(max_length=255)
    quantity = models.IntegerField()
    cause = models.CharField(max_length=255)
    customers = models.IntegerField()
    customer_qnt = models.IntegerField()
    photo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sp_pristroy'


class SpPristroyOrder(models.Model):
    owner = models.IntegerField()
    id_pristroy = models.IntegerField()
    title = models.TextField()
    date = models.IntegerField()
    price = models.IntegerField()
    customer_id = models.IntegerField()
    customer_name = models.TextField()
    quantity = models.IntegerField()
    paid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_pristroy_order'


class SpReviews(models.Model):
    user = models.IntegerField()
    uname = models.TextField(db_column='uName')  # Field name made lowercase.
    rtheme = models.CharField(db_column='rTheme', max_length=100)  # Field name made lowercase.
    date = models.IntegerField()
    rtext = models.TextField(db_column='rText')  # Field name made lowercase.
    cat = models.CharField(max_length=25)
    rdeleted = models.IntegerField(db_column='rDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sp_reviews'


class SpRyad(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.IntegerField()
    id_zp = models.IntegerField()
    title = models.CharField(max_length=255)
    articul = models.CharField(max_length=255)
    message = models.TextField()
    mess_edit = models.TextField()
    price = models.FloatField()
    size = models.CharField(max_length=255)
    duble = models.IntegerField()
    auto = models.IntegerField()
    spec = models.IntegerField()
    position = models.IntegerField()
    photo = models.CharField(max_length=255)
    cat = models.CharField(max_length=255)
    lock = models.IntegerField()
    autoblock = models.IntegerField()
    allblock = models.IntegerField()
    tempoff = models.IntegerField(db_column='tempOff')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sp_ryad'


class SpSize(models.Model):
    id_ryad = models.IntegerField()
    id_zp = models.IntegerField()
    name = models.CharField(max_length=255)
    user = models.IntegerField()
    duble = models.IntegerField()
    anonim = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_size'


class SpStatus(models.Model):
    name = models.CharField(max_length=255)
    discr = models.TextField()

    class Meta:
        managed = False
        db_table = 'sp_status'


class SpStorage(models.Model):
    id_stor = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    id_zp = models.IntegerField()
    on_site = models.IntegerField()
    email = models.CharField(max_length=100)
    is_mail = models.IntegerField()
    takeoff = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_storage'


class SpUrlCkeck(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.IntegerField()
    url = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    brend = models.CharField(max_length=255)
    date = models.CharField(max_length=20)
    city = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_url_ckeck'


class SpZakup(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.IntegerField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    rate = models.IntegerField()
    inform = models.CharField(max_length=500)
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
    date = models.IntegerField()
    type = models.IntegerField()
    file1 = models.CharField(max_length=255)
    file2 = models.CharField(max_length=255)
    file3 = models.CharField(max_length=255)
    price_name1 = models.TextField(blank=True, null=True)
    price_name2 = models.TextField(blank=True, null=True)
    price_name3 = models.TextField(blank=True, null=True)
    office = models.CharField(max_length=3000)
    paytype = models.IntegerField()
    hot = models.IntegerField()
    top = models.IntegerField()
    soonstop = models.IntegerField(db_column='soonStop')  # Field name made lowercase.
    datestop = models.CharField(db_column='dateStop', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sp_zakup'

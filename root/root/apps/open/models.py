# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import re


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


class GroupsTags(models.Model):
    id = models.AutoField(primary_key=True)
    name_rus = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups_tags'


class Lastfriends(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.IntegerField()
    friend = models.IntegerField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lastfriends'


class Message(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    user = models.IntegerField()
    contact = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_contacts'


class News(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    user = models.IntegerField()
    zp_id = models.IntegerField()
    office = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'office_set'


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profile'


class PunbbCategories(models.Model):
    id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=80)
    disp_position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'punbb_categories'


class PunbbCensoring(models.Model):
    id = models.AutoField(primary_key=True)
    search_for = models.CharField(max_length=60)
    replace_with = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'punbb_censoring'


class PunbbConfig(models.Model):
    id = models.AutoField(primary_key=True)
    conf_name = models.CharField(max_length=255)
    conf_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'punbb_config'


class PunbbForumPerms(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.IntegerField()
    forum_id = models.IntegerField()
    read_forum = models.IntegerField()
    post_replies = models.IntegerField()
    post_topics = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'punbb_forum_perms'
        unique_together = (('group_id', 'forum_id'),)


class PunbbForumSubscriptions(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    forum_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'punbb_forum_subscriptions'
        unique_together = (('user_id', 'forum_id'),)


class PunbbForums(models.Model):
    id = models.AutoField(primary_key=True)
    forum_name = models.CharField(max_length=80)
    forum_desc = models.TextField(blank=True, null=True)
    redirect_url = models.CharField(max_length=100, blank=True, null=True)
    moderators = models.TextField(blank=True, null=True)
    num_topics = models.PositiveIntegerField()
    num_posts = models.PositiveIntegerField()
    last_post = models.PositiveIntegerField(blank=True, null=True)
    last_post_id = models.PositiveIntegerField(blank=True, null=True)
    last_poster = models.CharField(max_length=200, blank=True, null=True)
    sort_by = models.IntegerField()
    disp_position = models.IntegerField()
    cat_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'punbb_forums'


class PunbbGroups(models.Model):
    g_id = models.AutoField(primary_key=True)
    g_title = models.CharField(max_length=50)
    g_user_title = models.CharField(max_length=50, blank=True, null=True)
    g_moderator = models.IntegerField()
    g_mod_edit_users = models.IntegerField()
    g_mod_rename_users = models.IntegerField()
    g_mod_change_passwords = models.IntegerField()
    g_mod_ban_users = models.IntegerField()
    g_read_board = models.IntegerField()
    g_view_users = models.IntegerField()
    g_post_replies = models.IntegerField()
    g_post_topics = models.IntegerField()
    g_edit_posts = models.IntegerField()
    g_delete_posts = models.IntegerField()
    g_delete_topics = models.IntegerField()
    g_set_title = models.IntegerField()
    g_search = models.IntegerField()
    g_search_users = models.IntegerField()
    g_send_email = models.IntegerField()
    g_post_flood = models.SmallIntegerField()
    g_search_flood = models.SmallIntegerField()
    g_email_flood = models.SmallIntegerField()
    g_pun_attachment_allow_download = models.IntegerField(blank=True, null=True)
    g_pun_attachment_allow_upload = models.IntegerField(blank=True, null=True)
    g_pun_attachment_allow_delete = models.IntegerField(blank=True, null=True)
    g_pun_attachment_allow_delete_own = models.IntegerField(blank=True, null=True)
    g_pun_attachment_upload_max_size = models.IntegerField(blank=True, null=True)
    g_pun_attachment_files_per_post = models.IntegerField(blank=True, null=True)
    g_pun_attachment_disallowed_extensions = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'punbb_groups'


class PunbbPosts(models.Model):
    poster = models.CharField(max_length=200)
    poster_id = models.PositiveIntegerField()
    poster_ip = models.CharField(max_length=39, blank=True, null=True)
    poster_email = models.CharField(max_length=80, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    hide_smilies = models.IntegerField()
    posted = models.PositiveIntegerField()
    edited = models.PositiveIntegerField(blank=True, null=True)
    edited_by = models.CharField(max_length=200, blank=True, null=True)
    topic_id = models.PositiveIntegerField()
    karma = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'punbb_posts'


class PunbbUsers(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    group_id = models.IntegerField(null=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=80)
    title = models.CharField(max_length=50, blank=True, null=True)
    realname = models.CharField(max_length=40, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    skype = models.CharField(max_length=100, blank=True, null=True)
    jabber = models.CharField(max_length=80, blank=True, null=True)
    icq = models.CharField(max_length=12, blank=True, null=True)
    msn = models.CharField(max_length=80, blank=True, null=True)
    aim = models.CharField(max_length=30, blank=True, null=True)
    yahoo = models.CharField(max_length=30, blank=True, null=True)
    actionuser = models.IntegerField(db_column='actionUser', blank=True, null=True)  # Field name made lowercase.
    signature = models.TextField(blank=True, null=True)
    disp_topics = models.PositiveIntegerField(blank=True, null=True)
    disp_posts = models.PositiveIntegerField(blank=True, null=True)
    email_setting = models.IntegerField()
    notify_with_post = models.IntegerField()
    auto_notify = models.IntegerField()
    show_smilies = models.IntegerField()
    show_img = models.IntegerField()
    show_img_sig = models.IntegerField()
    show_avatars = models.IntegerField()
    show_sig = models.IntegerField()
    access_keys = models.IntegerField()
    timezone = models.FloatField()
    dst = models.IntegerField()
    time_format = models.PositiveIntegerField()
    date_format = models.PositiveIntegerField()
    language = models.CharField(max_length=25)
    style = models.CharField(max_length=25)
    num_posts = models.PositiveIntegerField()
    last_post = models.PositiveIntegerField(blank=True, null=True)
    last_search = models.PositiveIntegerField(blank=True, null=True)
    last_email_sent = models.PositiveIntegerField(blank=True, null=True)
    registered = models.PositiveIntegerField()
    registration_ip = models.CharField(max_length=39)
    last_visit = models.PositiveIntegerField()
    admin_note = models.CharField(max_length=30, blank=True, null=True)
    activate_string = models.CharField(max_length=80, blank=True, null=True)
    activate_key = models.CharField(max_length=8, blank=True, null=True)
    avatar = models.PositiveIntegerField()
    avatar_width = models.PositiveIntegerField()
    avatar_height = models.PositiveIntegerField()
    city = models.PositiveIntegerField()
    region = models.PositiveIntegerField()
    country = models.PositiveIntegerField()
    phone = models.CharField(max_length=255)
    wm = models.FloatField()
    desc = models.CharField(max_length=255, blank=True)
    profile = models.TextField()
    karma = models.IntegerField()
    alertmail = models.PositiveIntegerField()
    voteusers = models.CharField(max_length=10000, blank=True)
    data_serv = models.TextField()
    promocode = models.CharField(db_column='promoCode', max_length=30)  # Field name made lowercase.
    stars_val = models.FloatField()
    stars = models.TextField(blank=True)
    rate = models.IntegerField()
    display_name = models.CharField(max_length=100, blank=True)
    user_url = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)

    # def __str__(self):
    #     return '{}'.format(str(self.id) + '-' + str(self.username) + '---' + str(self.realname))

    class Meta:
        managed = True
        db_table = 'punbb_users'
        ordering = ['id']
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"


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
    id = models.AutoField(primary_key=True)
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
    pass_field = models.CharField(db_column='pass',
                                  max_length=255)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'sp_add_org'


class SpAddpay(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
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
    # user = models.ForeignKey(PunbbUsers, on_delete=models.SET_NULL, null=True)
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
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class SpOrgorder(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.IntegerField()
    sum = models.FloatField()
    zp_id = models.IntegerField()
    user = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_orgorder'


class SpPristroy(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
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


class SpRate(models.Model):
    id = models.AutoField(primary_key=True)
    id_zp = models.IntegerField()
    rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_rate'


class SpReviews(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
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
    inform = models.TextField(blank=True)
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
    rekviz = models.TextField(max_length=1000)
    type = models.IntegerField()
    file1 = models.CharField(max_length=255, blank=True)
    file2 = models.CharField(max_length=255, blank=True)
    file3 = models.CharField(max_length=255, blank=True)
    price_name1 = models.CharField(max_length=100, blank=True, null=True)
    price_name2 = models.CharField(max_length=100, blank=True, null=True)
    price_name3 = models.CharField(max_length=100, blank=True, null=True)
    office = models.TextField()
    paytype = models.IntegerField()
    hot = models.IntegerField()
    top = models.IntegerField()
    soonstop = models.IntegerField(db_column='soonStop')  # Field name made lowercase.
    datestop = models.CharField(db_column='dateStop', max_length=50, blank=True)  # Field name made lowercase.

    # owner = models.ForeignKey('PunbbUsers', on_delete=models.SET_NULL, null=True, blank=True)

    # def __str__(self):
    #     return '{}'.format(str(self.id))

    def __str__(self):
        return 'templates/' + str(self.foto)
        # return self.title

    class Meta:
        managed = True
        db_table = 'sp_zakup'
        verbose_name = "Закупку"
        verbose_name_plural = "Закупкэ"


class Subs(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.IntegerField()
    table = models.IntegerField()
    lastcomm = models.IntegerField()
    id_post = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subs'


class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    name_rus = models.CharField(unique=True, max_length=255)
    name_eng = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tags'


class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.IntegerField()
    idvote = models.IntegerField()
    name = models.CharField(max_length=255)
    vote = models.IntegerField()
    select = models.IntegerField()
    cookie = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vote'

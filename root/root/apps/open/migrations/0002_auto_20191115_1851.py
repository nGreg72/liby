# Generated by Django 2.2.7 on 2019-11-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id_city', models.AutoField(primary_key=True, serialize=False)),
                ('id_region', models.PositiveIntegerField()),
                ('id_country', models.PositiveIntegerField()),
                ('city_name_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('city_name_en', models.CharField(max_length=255)),
                ('city_order', models.PositiveIntegerField()),
                ('show', models.IntegerField()),
            ],
            options={
                'db_table': 'cities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id_country', models.AutoField(primary_key=True, serialize=False)),
                ('country_name_ru', models.CharField(blank=True, max_length=50, null=True)),
                ('country_name_en', models.CharField(max_length=50)),
                ('country_iso', models.CharField(blank=True, max_length=2, null=True)),
                ('country_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('fgid', models.IntegerField()),
            ],
            options={
                'db_table': 'group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupsTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_rus', models.CharField(max_length=255)),
                ('name_eng', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'groups_tags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lastfriends',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('friend', models.IntegerField()),
                ('date', models.IntegerField()),
            ],
            options={
                'db_table': 'lastfriends',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_field', models.IntegerField(db_column='from')),
                ('to', models.IntegerField()),
                ('date', models.IntegerField()),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('view', models.IntegerField()),
                ('tresh', models.IntegerField()),
            ],
            options={
                'db_table': 'message',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MessageContacts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('contact', models.IntegerField()),
            ],
            options={
                'db_table': 'message_contacts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('cat', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('rate', models.IntegerField()),
                ('chpu', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=20)),
                ('show_date', models.IntegerField()),
                ('view', models.IntegerField()),
                ('tags_ru', models.TextField()),
                ('tags_en', models.TextField()),
                ('original_url', models.CharField(max_length=255)),
                ('thumbs', models.CharField(max_length=255)),
                ('comments', models.IntegerField()),
                ('moderate', models.IntegerField()),
                ('group', models.TextField()),
            ],
            options={
                'db_table': 'news',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('podcat', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('cat_chpu', models.CharField(max_length=255)),
                ('thumbs', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'office',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OfficeSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('zp_id', models.IntegerField()),
                ('office', models.IntegerField()),
            ],
            options={
                'db_table': 'office_set',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('num', models.IntegerField()),
            ],
            options={
                'db_table': 'profile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PunbbCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=80)),
                ('disp_position', models.IntegerField()),
            ],
            options={
                'db_table': 'punbb_categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PunbbCensoring',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('search_for', models.CharField(max_length=60)),
                ('replace_with', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'punbb_censoring',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PunbbConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('conf_name', models.CharField(max_length=255)),
                ('conf_value', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'punbb_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PunbbForumPerms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('group_id', models.IntegerField()),
                ('forum_id', models.IntegerField()),
                ('read_forum', models.IntegerField()),
                ('post_replies', models.IntegerField()),
                ('post_topics', models.IntegerField()),
            ],
            options={
                'db_table': 'punbb_forum_perms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PunbbForums',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('forum_name', models.CharField(max_length=80)),
                ('forum_desc', models.TextField(blank=True, null=True)),
                ('redirect_url', models.CharField(blank=True, max_length=100, null=True)),
                ('moderators', models.TextField(blank=True, null=True)),
                ('num_topics', models.PositiveIntegerField()),
                ('num_posts', models.PositiveIntegerField()),
                ('last_post', models.PositiveIntegerField(blank=True, null=True)),
                ('last_post_id', models.PositiveIntegerField(blank=True, null=True)),
                ('last_poster', models.CharField(blank=True, max_length=200, null=True)),
                ('sort_by', models.IntegerField()),
                ('disp_position', models.IntegerField()),
                ('cat_id', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'punbb_forums',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PunbbForumSubscriptions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.PositiveIntegerField()),
                ('forum_id', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'punbb_forum_subscriptions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PunbbGroups',
            fields=[
                ('g_id', models.AutoField(primary_key=True, serialize=False)),
                ('g_title', models.CharField(max_length=50)),
                ('g_user_title', models.CharField(blank=True, max_length=50, null=True)),
                ('g_moderator', models.IntegerField()),
                ('g_mod_edit_users', models.IntegerField()),
                ('g_mod_rename_users', models.IntegerField()),
                ('g_mod_change_passwords', models.IntegerField()),
                ('g_mod_ban_users', models.IntegerField()),
                ('g_read_board', models.IntegerField()),
                ('g_view_users', models.IntegerField()),
                ('g_post_replies', models.IntegerField()),
                ('g_post_topics', models.IntegerField()),
                ('g_edit_posts', models.IntegerField()),
                ('g_delete_posts', models.IntegerField()),
                ('g_delete_topics', models.IntegerField()),
                ('g_set_title', models.IntegerField()),
                ('g_search', models.IntegerField()),
                ('g_search_users', models.IntegerField()),
                ('g_send_email', models.IntegerField()),
                ('g_post_flood', models.SmallIntegerField()),
                ('g_search_flood', models.SmallIntegerField()),
                ('g_email_flood', models.SmallIntegerField()),
                ('g_pun_attachment_allow_download', models.IntegerField(blank=True, null=True)),
                ('g_pun_attachment_allow_upload', models.IntegerField(blank=True, null=True)),
                ('g_pun_attachment_allow_delete', models.IntegerField(blank=True, null=True)),
                ('g_pun_attachment_allow_delete_own', models.IntegerField(blank=True, null=True)),
                ('g_pun_attachment_upload_max_size', models.IntegerField(blank=True, null=True)),
                ('g_pun_attachment_files_per_post', models.IntegerField(blank=True, null=True)),
                ('g_pun_attachment_disallowed_extensions', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'punbb_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PunbbPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(max_length=200)),
                ('poster_id', models.PositiveIntegerField()),
                ('poster_ip', models.CharField(blank=True, max_length=39, null=True)),
                ('poster_email', models.CharField(blank=True, max_length=80, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('hide_smilies', models.IntegerField()),
                ('posted', models.PositiveIntegerField()),
                ('edited', models.PositiveIntegerField(blank=True, null=True)),
                ('edited_by', models.CharField(blank=True, max_length=200, null=True)),
                ('topic_id', models.PositiveIntegerField()),
                ('karma', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'punbb_posts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('id_country', models.PositiveIntegerField()),
                ('region_name_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('region_name_en', models.CharField(max_length=255)),
                ('region_order', models.PositiveIntegerField()),
                ('show', models.IntegerField()),
            ],
            options={
                'db_table': 'regions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.IntegerField()),
            ],
            options={
                'db_table': 'session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desk', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('group', models.IntegerField()),
            ],
            options={
                'db_table': 'setting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpAddOrg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('status', models.IntegerField()),
                ('region', models.IntegerField()),
                ('city', models.IntegerField()),
                ('country', models.IntegerField()),
                ('opyt', models.IntegerField()),
                ('post', models.IntegerField()),
                ('site', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('activate', models.IntegerField()),
                ('pass_field', models.CharField(db_column='pass', max_length=255)),
            ],
            options={
                'db_table': 'sp_add_org',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpAddpay',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zp_id', models.IntegerField()),
                ('user', models.IntegerField()),
                ('date', models.IntegerField()),
                ('date_user', models.CharField(max_length=255)),
                ('summ', models.FloatField()),
                ('summextra', models.FloatField(db_column='summExtra')),
                ('card', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('doplata', models.FloatField()),
                ('fldop', models.IntegerField()),
                ('transp', models.FloatField()),
                ('transpuser', models.FloatField(db_column='transpUser')),
                ('transpstatus', models.IntegerField(db_column='transpStatus')),
                ('bankname', models.CharField(db_column='bankName', max_length=10)),
                ('whopay', models.CharField(db_column='whoPay', max_length=50)),
                ('banknametransp', models.IntegerField(db_column='bankNameTransp')),
                ('whopaytransp', models.CharField(db_column='whoPayTransp', max_length=50)),
            ],
            options={
                'db_table': 'sp_addpay',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpAddpayorg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zp_id', models.IntegerField()),
                ('user', models.IntegerField()),
                ('date', models.IntegerField()),
                ('date_user', models.CharField(max_length=255)),
                ('summ', models.FloatField()),
                ('card', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'sp_addpayorg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpCat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('podcat', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('cat_chpu', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'sp_cat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpCatSub',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zakup', models.IntegerField()),
                ('cat', models.IntegerField()),
            ],
            options={
                'db_table': 'sp_cat_sub',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'sp_delivery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('discr', models.TextField()),
            ],
            options={
                'db_table': 'sp_level',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('user', models.IntegerField()),
                ('id_order', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('mess_edit', models.TextField()),
                ('color', models.CharField(max_length=255)),
                ('kolvo', models.IntegerField()),
                ('oversize', models.FloatField()),
                ('date', models.CharField(max_length=20)),
                ('uniqcod', models.CharField(max_length=20)),
                ('id_zp', models.IntegerField()),
                ('id_ryad', models.IntegerField()),
                ('dateunix', models.IntegerField()),
                ('status', models.IntegerField()),
                ('addrdelivery', models.IntegerField(db_column='addrDelivery')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'sp_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpOrgorder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.IntegerField()),
                ('sum', models.FloatField()),
                ('zp_id', models.IntegerField()),
                ('user', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'sp_orgorder',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpPristroy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('cat', models.IntegerField()),
                ('date', models.IntegerField()),
                ('price', models.IntegerField()),
                ('size', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('cause', models.CharField(max_length=255)),
                ('customers', models.IntegerField()),
                ('customer_qnt', models.IntegerField()),
                ('photo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'sp_pristroy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpPristroyOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('owner', models.IntegerField()),
                ('id_pristroy', models.IntegerField()),
                ('title', models.TextField()),
                ('date', models.IntegerField()),
                ('price', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('customer_name', models.TextField()),
                ('quantity', models.IntegerField()),
                ('paid', models.IntegerField()),
            ],
            options={
                'db_table': 'sp_pristroy_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpRate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_zp', models.IntegerField()),
                ('rate', models.IntegerField()),
            ],
            options={
                'db_table': 'sp_rate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpReviews',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('uname', models.TextField(db_column='uName')),
                ('rtheme', models.CharField(db_column='rTheme', max_length=100)),
                ('date', models.IntegerField()),
                ('rtext', models.TextField(db_column='rText')),
                ('cat', models.CharField(max_length=25)),
                ('rdeleted', models.IntegerField(db_column='rDeleted')),
            ],
            options={
                'db_table': 'sp_reviews',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpRyad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('id_zp', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('articul', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('mess_edit', models.TextField()),
                ('price', models.FloatField()),
                ('size', models.CharField(max_length=255)),
                ('duble', models.IntegerField()),
                ('auto', models.IntegerField()),
                ('spec', models.IntegerField()),
                ('position', models.IntegerField()),
                ('photo', models.CharField(max_length=255)),
                ('cat', models.CharField(max_length=255)),
                ('lock', models.IntegerField()),
                ('autoblock', models.IntegerField()),
                ('allblock', models.IntegerField()),
                ('tempoff', models.IntegerField(db_column='tempOff')),
            ],
            options={
                'db_table': 'sp_ryad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpSize',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_ryad', models.IntegerField()),
                ('id_zp', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('user', models.IntegerField()),
                ('duble', models.IntegerField()),
                ('anonim', models.IntegerField()),
            ],
            options={
                'db_table': 'sp_size',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('discr', models.TextField()),
            ],
            options={
                'db_table': 'sp_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpStorage',
            fields=[
                ('id_stor', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('customer_name', models.CharField(max_length=100)),
                ('id_zp', models.IntegerField()),
                ('on_site', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('is_mail', models.IntegerField()),
                ('takeoff', models.IntegerField()),
            ],
            options={
                'db_table': 'sp_storage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpUrlCkeck',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('url', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('brend', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=20)),
                ('city', models.IntegerField()),
            ],
            options={
                'db_table': 'sp_url_ckeck',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('table', models.IntegerField()),
                ('lastcomm', models.IntegerField()),
                ('id_post', models.IntegerField()),
            ],
            options={
                'db_table': 'subs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_rus', models.CharField(max_length=255, unique=True)),
                ('name_eng', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'tags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField()),
                ('idvote', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('vote', models.IntegerField()),
                ('select', models.IntegerField()),
                ('cookie', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PunbbUsers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('group_id', models.IntegerField(null=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('salt', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.CharField(max_length=80)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('realname', models.CharField(blank=True, max_length=40, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('skype', models.CharField(blank=True, max_length=100, null=True)),
                ('jabber', models.CharField(blank=True, max_length=80, null=True)),
                ('icq', models.CharField(blank=True, max_length=12, null=True)),
                ('msn', models.CharField(blank=True, max_length=80, null=True)),
                ('aim', models.CharField(blank=True, max_length=30, null=True)),
                ('yahoo', models.CharField(blank=True, max_length=30, null=True)),
                ('actionuser', models.IntegerField(blank=True, db_column='actionUser', null=True)),
                ('signature', models.TextField(blank=True, null=True)),
                ('disp_topics', models.PositiveIntegerField(blank=True, null=True)),
                ('disp_posts', models.PositiveIntegerField(blank=True, null=True)),
                ('email_setting', models.IntegerField()),
                ('notify_with_post', models.IntegerField()),
                ('auto_notify', models.IntegerField()),
                ('show_smilies', models.IntegerField()),
                ('show_img', models.IntegerField()),
                ('show_img_sig', models.IntegerField()),
                ('show_avatars', models.IntegerField()),
                ('show_sig', models.IntegerField()),
                ('access_keys', models.IntegerField()),
                ('timezone', models.FloatField()),
                ('dst', models.IntegerField()),
                ('time_format', models.PositiveIntegerField()),
                ('date_format', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=25)),
                ('style', models.CharField(max_length=25)),
                ('num_posts', models.PositiveIntegerField()),
                ('last_post', models.PositiveIntegerField(blank=True, null=True)),
                ('last_search', models.PositiveIntegerField(blank=True, null=True)),
                ('last_email_sent', models.PositiveIntegerField(blank=True, null=True)),
                ('registered', models.PositiveIntegerField()),
                ('registration_ip', models.CharField(max_length=39)),
                ('last_visit', models.PositiveIntegerField()),
                ('admin_note', models.CharField(blank=True, max_length=30, null=True)),
                ('activate_string', models.CharField(blank=True, max_length=80, null=True)),
                ('activate_key', models.CharField(blank=True, max_length=8, null=True)),
                ('avatar', models.PositiveIntegerField()),
                ('avatar_width', models.PositiveIntegerField()),
                ('avatar_height', models.PositiveIntegerField()),
                ('city', models.PositiveIntegerField()),
                ('region', models.PositiveIntegerField()),
                ('country', models.PositiveIntegerField()),
                ('phone', models.CharField(max_length=255)),
                ('wm', models.FloatField()),
                ('desc', models.CharField(blank=True, max_length=255)),
                ('profile', models.TextField()),
                ('karma', models.IntegerField()),
                ('alertmail', models.PositiveIntegerField()),
                ('voteusers', models.CharField(blank=True, max_length=10000)),
                ('data_serv', models.TextField()),
                ('promocode', models.CharField(db_column='promoCode', max_length=30)),
                ('stars_val', models.FloatField()),
                ('stars', models.TextField(blank=True)),
                ('rate', models.IntegerField()),
                ('display_name', models.CharField(blank=True, max_length=100)),
                ('user_url', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Пользователя',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'punbb_users',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SpZakup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('user', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('rate', models.IntegerField()),
                ('inform', models.TextField(blank=True)),
                ('level', models.IntegerField()),
                ('cat', models.IntegerField()),
                ('proc', models.IntegerField()),
                ('min', models.IntegerField()),
                ('mintype', models.IntegerField(db_column='minType')),
                ('curs', models.FloatField()),
                ('bonus', models.IntegerField()),
                ('dost', models.IntegerField()),
                ('status', models.IntegerField()),
                ('foto', models.CharField(max_length=255)),
                ('alertnews', models.IntegerField()),
                ('alertcomm', models.IntegerField()),
                ('comment', models.IntegerField()),
                ('id_check', models.IntegerField()),
                ('russia', models.CharField(max_length=100)),
                ('date', models.IntegerField()),
                ('rekviz', models.TextField(max_length=1000)),
                ('type', models.IntegerField()),
                ('file1', models.CharField(blank=True, max_length=255)),
                ('file2', models.CharField(blank=True, max_length=255)),
                ('file3', models.CharField(blank=True, max_length=255)),
                ('price_name1', models.CharField(blank=True, max_length=100, null=True)),
                ('price_name2', models.CharField(blank=True, max_length=100, null=True)),
                ('price_name3', models.CharField(blank=True, max_length=100, null=True)),
                ('office', models.TextField()),
                ('paytype', models.IntegerField()),
                ('hot', models.IntegerField()),
                ('top', models.IntegerField()),
                ('soonstop', models.IntegerField(db_column='soonStop')),
                ('datestop', models.CharField(blank=True, db_column='dateStop', max_length=50)),
            ],
            options={
                'verbose_name': 'Закупку',
                'verbose_name_plural': 'Закупкэ',
                'db_table': 'sp_zakup',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='DB',
        ),
    ]

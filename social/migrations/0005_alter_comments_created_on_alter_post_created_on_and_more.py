# Generated by Django 4.0.2 on 2022-02-13 10:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_alter_comments_created_on_alter_post_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 10, 21, 20, 625230, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 10, 21, 20, 625230, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 13, 10, 21, 20, 626230, tzinfo=utc), null=True),
        ),
    ]

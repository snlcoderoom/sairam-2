# Generated by Django 3.2.8 on 2022-03-24 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_sivam_about_page_sivam_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='sivam_about_page',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

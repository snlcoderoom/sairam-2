# Generated by Django 3.2.8 on 2022-03-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20211117_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='aname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
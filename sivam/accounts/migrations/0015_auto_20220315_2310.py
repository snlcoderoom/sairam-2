# Generated by Django 3.2.8 on 2022-03-15 17:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20220314_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='date',
            new_name='date_of_activity',
        ),
        migrations.AlterField(
            model_name='report',
            name='write_up',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

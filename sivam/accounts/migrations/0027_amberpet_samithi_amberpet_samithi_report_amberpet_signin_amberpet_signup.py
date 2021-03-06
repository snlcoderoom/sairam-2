# Generated by Django 3.2.8 on 2022-03-23 10:43

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0026_landing_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='amberpet_samithi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('about_samithi', ckeditor.fields.RichTextField()),
                ('name', models.CharField(blank=True, max_length=100)),
                ('designation', models.CharField(blank=True, max_length=50)),
                ('mobile', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('address', models.TextField(blank=True, max_length=150)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='amberpet_samithi_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_activity', models.CharField(blank=True, max_length=50)),
                ('date_of_activity', models.DateField(blank=True, default=datetime.datetime.now)),
                ('place', models.CharField(blank=True, max_length=50)),
                ('wings', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Spiritual', 'Spiritual'), ('Educational', 'Educational'), ('Service', 'Service')], max_length=150)),
                ('spiritual_activity', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Bhajan', 'Bhajan'), ('Nagarsankeertan', 'Nagarsankeertan'), ('Studycircle', 'Studycircle'), ('Namasmarana', 'Namasmarana'), ('Japa', 'Japa'), ('Meditation', 'Meditation'), ('Spiritualclass', 'Spiritualclass'), ('Lectures', 'Lectures'), ('Seminars', 'Seminars'), ('Sadhanacamps', 'Sadhanacamps')], max_length=500)),
                ('educational_activity', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Balvikas', 'Balvikas'), ('Gems', 'Gems'), ('Parenting Workshop', 'Parenting Workshop')], max_length=500)),
                ('service_activity', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Narayanaseva', 'Narayanaseva'), ('Amrutha Kalusams Distribution', 'Amrutha Kalusams Distribution'), ('Blanket Distribution', 'Blanket Distribution'), ('Blood Donation Camp', 'Blood Donation Camp'), ('Blood Group Test', 'Blood Group Test'), ('Shirts Distribution', 'Shirts Distribution'), ('Sarees Distribution', 'Sarees Distribution'), ('Sai Protein', 'Sai Protein'), ('Medicalcamp', 'Medicalcamp'), ('Bhima Ratha Shanthi', 'Bhima Ratha Shanthi'), ('Veterinary Camp', 'Veterinary Camp'), ('Educational_assistance', 'Educational_assistance'), ('Skill_Development Program', 'Skill_Development Program'), ('Hospital_Service', 'Hospital_Service'), ('Oldage_Home', 'Oldage_Home'), ('Orphanage_Service', 'Orphanage_Service'), ('Gramaseva', 'Gramaseva'), ('Providing_relief', 'Providing_relief'), ('Other Service', 'Other Service')], max_length=500)),
                ('write_up', ckeditor.fields.RichTextField()),
                ('photo1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('submitted_by', models.CharField(blank=True, max_length=50)),
                ('mobile', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='amberpet_signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=150)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='amberpet_signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=150)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

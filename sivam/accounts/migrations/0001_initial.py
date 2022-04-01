# Generated by Django 3.2.8 on 2021-11-11 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('samithi', models.CharField(blank=True, choices=[('Ameerpet', 'Ameerpet'), ('Amberpet', 'Amberpet'), ('Dilsukhnagar', 'Dilsukhnagar'), ('Gandhinagar', 'Gandhinagar'), ('Himayathnagar', 'Himayathnagar'), ('Kachiguda', 'Kachiguda'), ('Khairtabad', 'Khairtabad'), ('Koti', 'Koti'), ('Mehdipatnam', 'Mehdipatnam'), ('Marredpally', 'Marredpally'), ('Prasanthi Nagar', 'Prasanthi Nagar'), ('Seethaphalmandi', 'Seethaphalmandi'), ('S R Nagar', 'S R Nagar'), ('Tarnaka', 'Tarnaka'), ('Vengal Rao Nagar', 'Vengal Rao Nagar'), ('Vidya Nagar', 'Vidya Nagar')], max_length=50)),
                ('place', models.CharField(blank=True, max_length=50)),
                ('form_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('to_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('spiritual_activity', models.CharField(blank=True, choices=[('Bhajan', 'Bhajan'), ('Nagarsankeertan', 'Nagarsankeertan'), ('Studycircle', 'Studycircle'), ('Namasmarana', 'Namasmarana'), ('Japa', 'Japa'), ('Meditation', 'Meditation'), ('Spiritualclass', 'Spiritualclass'), ('Lectures', 'Lectures'), ('Seminars', 'Seminars'), ('Sadhanacamps', 'Sadhanacamps')], max_length=50)),
                ('educational_activity', models.CharField(blank=True, choices=[('Balvikas', 'Balvikas'), ('Gems', 'Gems'), ('Goodparenting', 'Goodparenting')], max_length=50)),
                ('service_activity', models.CharField(blank=True, choices=[('Narayanaseva', 'Narayanaseva'), ('Medicalcamp', 'Medicalcamp'), ('Veterinarycamp', 'Veterinarycamp'), ('Educational_assistance', 'Educational_assistance'), ('vocational_Training', 'Vocational_Training'), ('Skill_Development', 'Skill_Development'), ('hospital_seva', 'hospital_seva'), ('Oldage_home', 'Oldage_home'), ('Gramaseva', 'Gramaseva'), ('Providing_relief', 'Providing_relief')], max_length=50)),
                ('write_up', models.TextField(blank=True, max_length=500)),
                ('hours', models.CharField(blank=True, max_length=50)),
                ('pahoto1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('pahoto2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('pahoto3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('pahoto4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('pahoto5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('pahoto6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('pahoto7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('pahoto8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('submitted_by', models.CharField(blank=True, max_length=50)),
                ('mobile', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
            ],
        ),
    ]

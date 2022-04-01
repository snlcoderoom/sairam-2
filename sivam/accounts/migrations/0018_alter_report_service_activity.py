# Generated by Django 3.2.8 on 2022-03-16 08:41

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20220316_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='service_activity',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Narayanaseva', 'Narayanaseva'), ('Amrutha Kalusams Distribution', 'Amrutha Kalusams Distribution'), ('Blanket Distribution', 'Blanket Distribution'), ('Blood Donation Camp', 'Blood Donation Camp'), ('Blood Group Test', 'Blood Group Test'), ('Shirts Distribution', 'Shirts Distribution'), ('Sarees Distribution', 'Sarees Distribution'), ('Sai Protein', 'Sai Protein'), ('Medicalcamp', 'Medicalcamp'), ('Bhima Ratha Shanthi', 'Bhima Ratha Shanthi'), ('Veterinary Camp', 'Veterinary Camp'), ('Educational_assistance', 'Educational_assistance'), ('Skill_Development Program', 'Skill_Development Program'), ('Hospital_Service', 'Hospital_Service'), ('Oldage_Home', 'Oldage_Home'), ('Orphanage_Service', 'Orphanage_Service'), ('Gramaseva', 'Gramaseva'), ('Providing_relief', 'Providing_relief')], max_length=500),
        ),
    ]

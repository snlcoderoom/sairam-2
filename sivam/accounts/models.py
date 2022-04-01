from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField


# Create your models here.

samithi_choices = (
    ('Ameerpet', 'Ameerpet'),
    ('Amberpet', 'Amberpet'),
    ('Dilsukhnagar', 'Dilsukhnagar'),
    ('Gandhinagar', 'Gandhinagar'),
    ('Himayathnagar', 'Himayathnagar'),
    ('Kachiguda', 'Kachiguda'),
    ('Khairtabad', 'Khairtabad'),
    ('Koti', 'Koti'),
    ('Mehdipatnam', 'Mehdipatnam'),
    ('Marredpally', 'Marredpally'),
    ('Prasanthi Nagar', 'Prasanthi Nagar'),
    ('Seethaphalmandi', 'Seethaphalmandi'),
    ('S R Nagar', 'S R Nagar'),
    ('Tarnaka', 'Tarnaka'),
    ('Vengal Rao Nagar', 'Vengal Rao Nagar'),
    ('Vidya Nagar', 'Vidya Nagar'),

)

activity_choices = (
    ('Spiritual', 'Spiritual'),
    ('Educational', 'Educational'),
    ('Service', 'Service'),

)



spiritual_choices = (
    ('Bhajan', 'Bhajan'),
    ('Nagarsankeertan', 'Nagarsankeertan'),
    ('Studycircle', 'Studycircle'),
    ('Namasmarana', 'Namasmarana'),
    ('Japa', 'Japa'),
    ('Meditation', 'Meditation'),
    ('Spiritualclass', 'Spiritualclass'),
    ('Lectures', 'Lectures'),
    ('Seminars', 'Seminars'),
    ('Sadhanacamps', 'Sadhanacamps'),


)


educational_choices = (
    ('Balvikas', 'Balvikas'),
    ('Gems', 'Gems'),
    ('Parenting Workshop', 'Parenting Workshop'),


)


service_choices = (
    ('Narayanaseva', 'Narayanaseva'),
    ('Amrutha Kalusams Distribution', 'Amrutha Kalusams Distribution'),
    ('Blanket Distribution', 'Blanket Distribution'),
    ('Blood Donation Camp', 'Blood Donation Camp'),
    ('Blood Group Test', 'Blood Group Test'),
    ('Shirts Distribution', 'Shirts Distribution'),
    ('Sarees Distribution', 'Sarees Distribution'),
    ('Sai Protein', 'Sai Protein'),
    ('Medicalcamp', 'Medicalcamp'),
    ('Bhima Ratha Shanthi', 'Bhima Ratha Shanthi'),
    ('Veterinary Camp', 'Veterinary Camp'),
    ('Educational_assistance', 'Educational_assistance'),
    ('Skill_Development Program', 'Skill_Development Program'),
    ('Hospital_Service', 'Hospital_Service'),
    ('Oldage_Home', 'Oldage_Home'),
    ('Orphanage_Service', 'Orphanage_Service'),
    ('Gramaseva', 'Gramaseva'),
    ('Providing_relief', 'Providing_relief'),
    ('Other Service', 'Other Service'),

)


class Samathi(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # samthi = models.CharField(choices=samithi_choices, max_length=50, blank=True)
    Amberpet = models.CharField(max_length=100, blank=True)
    Ameerpet = models.CharField(max_length=100, blank=True)
    Dilsuknagar = models.CharField(max_length=100, blank=True)
    Himayathnagar = models.CharField(max_length=100, blank=True)
    Gandhinagar = models.CharField(max_length=100, blank=True)
    Kachiguda = models.CharField(max_length=100, blank=True)
    Khartabad = models.CharField(max_length=100, blank=True)
    Koti = models.CharField(max_length=100, blank=True)
    Marredpally = models.CharField(max_length=100, blank=True)
    Mehdipatnam = models.CharField(max_length=100, blank=True)
    Prasanthnagar = models.CharField(max_length=100, blank=True)
    Sitaphalmandi = models.CharField(max_length=100, blank=True)
    SRnagar = models.CharField(max_length=100, blank=True)
    Tarnaka = models.CharField(max_length=100, blank=True)
    Vengalraonagar = models.CharField(max_length=100, blank=True)
    Vidyanagar = models.CharField(max_length=100, blank=True)


class Report (models.Model):
    samithi = models.ForeignKey(Samathi, on_delete=models.CASCADE, null=True)
    name_of_the_activity = models.CharField(max_length=50, blank=True)
    date_of_activity = models.DateField(default=datetime.now, blank=True)
    samithi = models.CharField(choices=samithi_choices, max_length=50, blank=True)
    place = models.CharField(max_length=50, blank=True)
    from_time = models.TimeField(default=datetime.now, blank=True)
    to_time = models.TimeField(default=datetime.now, blank=True)
    # activity = models.CharField(choices=activity_choices, max_length=50, blank=True)
    wings = MultiSelectField(choices=activity_choices, max_length=150, blank=True)
    spiritual_activity = MultiSelectField(choices=spiritual_choices, max_length=500, blank=True)
    educational_activity = MultiSelectField(choices=educational_choices, max_length=500, blank=True)
    service_activity = MultiSelectField(choices=service_choices, max_length=500, blank=True)
    write_up = RichTextField()
    hours = models.CharField(max_length=50, blank=True)
    pahoto1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    pahoto2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    pahoto3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    pahoto4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    pahoto5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    pahoto6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    pahoto7 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    pahoto8 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    # image = models.FileField(null=True)
    submitted_by = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    is_recent = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class Samithi_office_bearers(models.Model):
    samithi = models.ForeignKey(Samathi, on_delete=models.CASCADE,null=True)
    slno = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    address = models.TextField(max_length=150, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    write_up = models.TextField(max_length=1500, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

class Sivam_about_page(models.Model):
    sivam_img = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    title = models.CharField(max_length=100, blank=True)
    history = RichTextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

class Dist_office_bearers(models.Model):
    slno = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    address = models.TextField(max_length=150, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

class Sivam_Events(models.Model):
    name_of_the_activity = models.CharField(max_length=50, blank=True)
    date_of_activity = models.DateField(default=datetime.now, blank=True)
    write_up = RichTextField()
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name_of_the_activity

class About_HNR_Samithi(models.Model):
    samithi_title = models.CharField(max_length=100, blank=True)
    description = RichTextField()
    main_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.samithi_title


class Carousel(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=150)
    action_name = models.CharField(max_length=50)
    link = models.TextField(null=True, blank=True)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Landing_page(models.Model):
    about_sivam = RichTextField()
    wings = RichTextField()
    s_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    sw_heading = models.CharField(max_length=150)
    sw_para = models.CharField(max_length=150)
    e_photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    ew_heading = models.CharField(max_length=150)
    ew_para = models.CharField(max_length=150)
    s_photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    swg_heading = models.CharField(max_length=150)
    swg_para = models.CharField(max_length=150)

    def __str__(self):
        return self.about_sivam

class Sivam_spw_page(models.Model):
    sivam_img = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    title = models.CharField(max_length=100, blank=True)
    write_up = RichTextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

class Sivam_ew_page(models.Model):
    sivam_img = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    title = models.CharField(max_length=100, blank=True)
    write_up = RichTextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

class Sivam_srw_page(models.Model):
    sivam_img = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    title = models.CharField(max_length=100, blank=True)
    write_up = RichTextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)


# AMBERPER SAMITHI START
class amberpet_samithi(models.Model):
    samithi = models.ForeignKey(Samathi, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=True)
    main_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    about_samithi = RichTextField()
    # name = models.CharField(max_length=100, blank=True)
    # designation = models.CharField(max_length=50, blank=True)
    # mobile = models.CharField(max_length=50, blank=True)
    # email = models.EmailField(max_length=50, blank=True)
    # address = models.TextField(max_length=150, blank=True)
    # created_date = models.DateTimeField(default=datetime.now, blank=True)
    samithi = models.CharField(choices=samithi_choices, max_length=50, blank=True,null=True)
    def __str__(self):
        return self.title

class as_office_bearers(models.Model):
    samithi = models.ForeignKey(Samathi, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    address = models.TextField(max_length=150, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    samithi = models.CharField(choices=samithi_choices, max_length=50, blank=True,null=True)
    def __str__(self):
        return self. samithi

class amberpet_samithi_report(models.Model):
    samithi = models.ForeignKey(Samathi, on_delete=models.CASCADE, null=True)
    name_of_the_activity = models.CharField(max_length=50, blank=True)
    date_of_activity = models.DateField(default=datetime.now, blank=True)
    place = models.CharField(max_length=50, blank=True)
    wings = MultiSelectField(choices=activity_choices, max_length=150, blank=True)
    spiritual_activity = MultiSelectField(choices=spiritual_choices, max_length=500, blank=True)
    educational_activity = MultiSelectField(choices=educational_choices, max_length=500, blank=True)
    service_activity = MultiSelectField(choices=service_choices, max_length=500, blank=True)
    write_up = RichTextField()
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    submitted_by = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    samithi = models.CharField(choices=samithi_choices, max_length=50, blank=True,null=True)
    title = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.samithi
# AMBERPER SAMITHI END

class Seva_Report(models.Model):
    samithi = models.CharField(choices=samithi_choices, max_length=50, blank=True)
    activity_name = models.CharField(max_length=50, blank=True)
    place = models.CharField(max_length=50, blank=True)
    content = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.samithi

class Register_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    samithi = models.CharField(choices=samithi_choices, max_length=50, blank=True)
    def __str__(self):
        return self.samithi


class samithi_login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    samithi = models.CharField(choices=samithi_choices, max_length=50, blank=True)
    title = models.CharField(max_length=75, blank=True)
    def __str__(self):
        return self.samithi

class Signup_User(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    samithi = models.CharField(choices=samithi_choices, max_length=50, blank=True)
    mobile = models.IntegerField(null=True)
    image = models.FileField(null=True)
    reg = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.user.username+" "+self.reg









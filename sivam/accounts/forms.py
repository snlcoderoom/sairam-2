from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Report,Samithi_office_bearers,\
    Dist_office_bearers,Sivam_Events,About_HNR_Samithi,Landing_page,Carousel,\
    amberpet_samithi,as_office_bearers,amberpet_samithi_report,Sivam_about_page,\
    Seva_Report,Sivam_spw_page,Sivam_ew_page,Sivam_srw_page

class ReportModelForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('name_of_the_activity', 'date_of_activity', 'samithi', 'place', 'from_time', 'to_time',
                  'wings', 'spiritual_activity', 'educational_activity',
                  'service_activity', 'write_up', 'hours', 'pahoto1', 'pahoto2',
                  'pahoto3', 'pahoto4', 'pahoto5', 'pahoto6', 'pahoto7', 'pahoto8',
                  'submitted_by', 'mobile', 'email')

        labels = {
            'name_of_the_activity': 'Name of the Activity',
            'date_of_activity' : 'Date of Activity',
            'samithi': 'Name of the Samithi',
            'place': 'Acivity done at',
            'from_time': 'Activity begin Time',
            'to_time': 'Activity end Time',
            'wings': 'Service Wings covered in Activity',
            'spiritual_activity': 'Spiritual Activities',
            'educational_activity': 'Educational Activities',
            'service_activity': 'Service Activities',
            'write_up': 'Details of Service activity',
            'hours': 'Service Hours',
            'pahoto1': 'Photo',
            'pahoto2': 'Photo',
            'pahoto3': 'Photo',
            'pahoto4': 'Photo',
            'pahoto5': 'Photo',
            'pahoto6': 'Photo',
            'pahoto7': 'Photo',
            'pahoto8': 'Photo',
            'submitted_by': 'Report Submitted by',
            'mobile': 'Mobile Number',
            'email': 'Email Id',

        }

        widgets = {
            'name_of_the_activity':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_activity': forms.DateInput(attrs={'class': 'form-control'}),
            'samithi': forms.Select(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'from_time': forms.TimeInput(attrs={'class': 'form-control'}),
            'to_time': forms.TimeInput(attrs={'class': 'form-control'}),
            'wings': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'spiritual_activity': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'educational_activity': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'service_activity': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'write_up': forms.Textarea(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),
            'hours': forms.TextInput(attrs={'class': 'form-control'}),
            # 'pahoto1': forms.ImageField(attrs={'class': 'form-control'}),
            # 'pahoto2': forms.ImageField(attrs={'class': 'form-control'}),
            # 'pahoto3': forms.ImageField(attrs={'class': 'form-control'}),
            # 'pahoto4': forms.ImageField(attrs={'class': 'form-control'}),
            # 'pahoto5': forms.ImageField(attrs={'class': 'form-control'}),
            # 'pahoto6': forms.ImageField(attrs={'class': 'form-control'}),
            # 'pahoto7': forms.ImageField(attrs={'class': 'form-control'}),
            # 'pahoto8': forms.ImageField(attrs={'class': 'form-control'}),
            'submitted_by': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class Samithi_office_bearersModelForm(forms.ModelForm):
    class Meta:
        model = Samithi_office_bearers
        fields = ('name', 'designation', 'mobile', 'email', 'address')


        labels = {
            'name': 'Full Name ',
            'designation': 'Designation',
            'mobile': 'Mobile Number',
            'email': 'Email Id',
            'address': 'Address',
                   }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
                   }

class Dist_office_bearersModelForm(forms.ModelForm):
    class Meta:
        model = Dist_office_bearers
        fields = ('name', 'designation', 'mobile', 'email', 'address')

        labels = {
            'name': 'Full Name ',
            'designation': 'Designation',
            'mobile': 'Mobile Number',
            'email': 'Email Id',
            'address': 'Address',
                   }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
                   }

class Sivam_EventsModelForm(forms.ModelForm):
    class Meta:
        model = Sivam_Events
        fields = ('name_of_the_activity', 'date_of_activity', 'write_up', 'photo1', 'photo2',
                  'photo3', 'photo4', 'photo5', 'photo6','photo7','photo8')

        labels = {
            'name_of_the_activity': 'Name of the Event ',
            'date_of_activity': 'Date of the Event',
            'write_up': 'Event Description',
            'photo1': 'Photo',
            'photo2': 'Photo',
            'photo3': 'Photo',
            'photo4': 'Photo',
            'photo5': 'Photo',
            'photo6': 'Photo',
            'photo7': 'Photo',
            'photo8': 'Photo',
                   }

        widgets = {
            'name_of_the_activity': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_activity': forms.DateInput(attrs={'class': 'form-control'}),
            'write_up': forms.Textarea(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),

                   }

class About_HNR_SamithiModelForm(forms.ModelForm):
    class Meta:
        model = About_HNR_Samithi
        fields = ('samithi_title', 'description', 'main_img','created_date')

        labels = {
            'samithi_title': 'Heading',
            'description': 'Samithi History and Description',
            'main_img': 'Main Image',
            'created_date': 'Date',

                   }

        widgets = {
            'samithi_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),
            # 'main_img': forms.ImageField(attrs={'class': 'form-control'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control'}),
                   }

class Landing_pageModelForm(forms.ModelForm):
    class Meta:
        model = Landing_page
        fields = ('about_sivam', 'wings', 's_photo1','sw_heading',
                  'sw_para','e_photo2','ew_heading','ew_para',
                  's_photo3','swg_heading','swg_para')

        labels = {
            'about_sivam': 'About Sivam',
            'wings': 'Wings of the Organisation',
            's_photo1': 'Spiritual Wing Image',
            'sw_heading': 'Spiritual Wing Heading',
            'sw_para': 'Two line description about Spiritual Wing',
            'e_photo2': 'Educational Wing Image',
            'ew_heading': 'Educational Wing Heading',
            'ew_para': 'Two line description about Educational Wing',
            's_photo3': 'Service Wing Image',
            'swg_heading': 'Service Wing Heading',
            'swg_para': 'Two line description about Service Wing',

                   }

        widgets = {
            'about_sivam': forms.Textarea(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),
            'wings': forms.Textarea(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),
            'sw_heading': forms.TextInput(attrs={'class': 'form-control'}),
            'sw_para': forms.TextInput(attrs={'class ': 'form-control'}),
            'ew_heading': forms.TextInput(attrs={'class': 'form-control'}),
            'ew_para': forms.TextInput(attrs={'class ': 'form-control'}),
            'swg_heading': forms.TextInput(attrs={'class': 'form-control'}),
            'swg_para': forms.TextInput(attrs={'class ': 'form-control'}),
                   }

class CarouselModelForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ('image', 'title', 'action_name', 'link', 'sub_title')

        labels = {
            'image': 'Upload Image ',
            'title': 'Saying',
            'action_name': 'Action Saying',
            'link': 'Link',
            'sub_title': 'Subtitle',
                   }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'action_name': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control'}),

                   }

class Sivam_about_pageModelForm(forms.ModelForm):
    class Meta:
        model = Sivam_about_page
        fields = ('sivam_img','title', 'history')

        labels = {
            'sivam_img': 'Upload Image ',
            'title': 'Heading',
            'history': 'History',
                   }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'history': forms.Textarea(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),
                   }

class Sivam_spw_pageModelForm(forms.ModelForm):
    class Meta:
        model = Sivam_spw_page
        fields = ('sivam_img','title', 'write_up')

        labels = {
            'sivam_img': 'Upload Image ',
            'title': 'Heading',
            'write_up': 'History',
                   }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'write_up': forms.Textarea(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),
                   }


class Sivam_ew_pageModelForm(forms.ModelForm):
    class Meta:
        model = Sivam_ew_page
        fields = ('sivam_img','title', 'write_up')

        labels = {
            'sivam_img': 'Upload Image ',
            'title': 'Heading',
            'write_up': 'History',
                   }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'write_up': forms.Textarea(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),
                   }


class Sivam_srw_pageModelForm(forms.ModelForm):
    class Meta:
        model = Sivam_srw_page
        fields = ('sivam_img','title', 'write_up')

        labels = {
            'sivam_img': 'Upload Image ',
            'title': 'Heading',
            'write_up': 'History',
                   }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'write_up': forms.Textarea(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),
                   }

class Seva_ReportModelForm(forms.ModelForm):
    class Meta:
        model = Seva_Report
        fields = ('samithi','activity_name', 'place','content')

        labels = {
            'samithi': 'Samithi Name ',
            'activity_name': 'Name of the Activity',
            'place': 'Place of the Activity',
            'content': 'Writeup',

                   }

        widgets = {
            'samithi': forms.Select(attrs={"name": "select_0","class": "form-control"}),
            'activity_name': forms.TextInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),

                   }







# AMBERPET SAMITHI FORMS START:

class amberpet_samithiModelForm(forms.ModelForm):
    class Meta:
        model = amberpet_samithi
        fields = ('samithi','title','main_img', 'about_samithi')

        labels = {
            'samithi': 'Name of the Samithi',
            'title': 'Samithi Title',
            'main_img': 'Upload Image',
            'about_samithi': 'About Samithi',

                  }

        widgets = {
             'samithi': forms.Select(attrs={"name": "select_0","class": "form-control"}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'about_samithi': forms.Textarea(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),

                   }

class as_office_bearersModelForm(forms.ModelForm):
    class Meta:
        model = as_office_bearers
        fields = ('samithi','name', 'designation', 'mobile', 'email', 'address')

        labels = {
            'samithi': 'Name of the Samithi ',
            'name': 'Full Name ',
            'designation': 'Designation',
            'mobile': 'Mobile Number',
            'email': 'Email Id',
            'address': 'Address',
        }

        widgets = {
            'samithi': forms.Select(attrs={"name": "select_0", "class": "form-control"}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class amberpet_samithi_reportModelForm(forms.ModelForm):
    class Meta:
        model = amberpet_samithi_report
        fields = ('samithi','name_of_the_activity', 'date_of_activity', 'place', 'wings', 'spiritual_activity', 'educational_activity',
                  'service_activity', 'write_up', 'photo1', 'photo2',
                  'photo3', 'photo4', 'photo5', 'photo6', 'photo7', 'photo8',
                  'submitted_by', 'mobile', 'email')

        labels = {
            'samithi': 'Name of the Samithi',
            'name_of_the_activity': 'Name of the Activity',
            'date_of_activity' : 'Date of Activity',
            'place': 'Acivity done at',
            'wings': 'Service Wings covered in Activity',
            'spiritual_activity': 'Spiritual Activities',
            'educational_activity': 'Educational Activities',
            'service_activity': 'Service Activities',
            'write_up': 'Details of Service activity',
            'photo1': 'Photo',
            'photo2': 'Photo',
            'photo3': 'Photo',
            'photo4': 'Photo',
            'photo5': 'Photo',
            'photo6': 'Photo',
            'photo7': 'Photo',
            'photo8': 'Photo',
            'submitted_by': 'Report Submitted by',
            'mobile': 'Mobile Number',
            'email': 'Email Id',

        }

        widgets = {
            'samithi': forms.Select(attrs={"name": "select_0","class": "form-control"}),
            'name_of_the_activity':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_activity': forms.DateInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'wings': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'spiritual_activity': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'educational_activity': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'service_activity': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'write_up': forms.Textarea(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),
            # 'photo1': forms.FileField(attrs={'class': 'form-control'}),
            # 'photo2': forms.FileField(attrs={'class': 'form-control'}),
            # 'photo3': forms.FileField(attrs={'class': 'form-control'}),
            # 'photo4': forms.FileField(attrs={'class': 'form-control'}),
            # 'photo5': forms.FileField(attrs={'class': 'form-control'}),
            # 'photo6': forms.FileField(attrs={'class': 'form-control'}),
            # 'photo7': forms.FileField(attrs={'class': 'form-control'}),
            # 'photo8': forms.FileField(attrs={'class': 'form-control'}),
            'submitted_by': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


# class RegisterUserForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
#
#     def __init__(self, *args, **kwargs):
#         super(RegisterUserForm, self).__init__(*args, **kwargs)
#
#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['class'] = 'form-control'


# class Register_UserModelForm(forms.ModelForm):
#     class Meta:
#         model = Register_User
#         fields = ('samithi',)
#
#         labels = {
#             'samithi': 'Name of the Samithi', }
#
#         widgets = {
#              'samithi': forms.Select(attrs={"name": "select_0","class": "form-control"}),


# class samithi_loginModelForm(forms.ModelForm):
#     class Meta:
#         model = samithi_login
#         fields = ('samithi','username','password')
#
#         labels = {
#             'samithi': 'Name of the Samithi',
#             'username': 'User Name',
#             'password': 'Password',
#
#                   }
#
#         widgets = {
#              'samithi': forms.Select(attrs={"name": "select_0","class": "form-control"}),
#              'username': forms.TextInput(attrs={'class': 'form-control'}),
#              'password': forms.PasswordInput(attrs={'class': 'form-control django-ckeditor-widget ckeditor'}),
#
#                    }


# AMBERPET SAMITHI FORMS END:

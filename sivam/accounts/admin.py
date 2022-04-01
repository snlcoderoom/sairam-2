from django.contrib import admin
from .models import Report, Samathi, Samithi_office_bearers,Dist_office_bearers,\
    Sivam_Events,About_HNR_Samithi,Carousel,Landing_page,amberpet_samithi,amberpet_samithi_report,\
    Sivam_about_page,Contact, Sivam_spw_page, Sivam_ew_page,Sivam_srw_page,Seva_Report,samithi_login


# class SamathiAdmin(admin.ModelAdmin):
#     list_display=['id','user','samthi',]

class ReportAdmin(admin.ModelAdmin):
    list_display=['id', 'created_date', 'name_of_the_activity','samithi','place','pahoto1', 'submitted_by','mobile', 'email',]

class Samithi_office_bearersAdmin(admin.ModelAdmin):
    list_display=['id', 'created_date', 'name','designation','mobile','created_date']

class Dist_office_bearersAdmin(admin.ModelAdmin):
    list_display=['id', 'created_date', 'name','designation','mobile','created_date']

class Sivam_EventsAdmin(admin.ModelAdmin):
    list_display=['id', 'name_of_the_activity', 'date_of_activity','created_date']

class About_HNR_SamithiAdmin(admin.ModelAdmin):
    list_display=['id', 'samithi_title']

class ContactAdmin(admin.ModelAdmin):
    list_display=['id', 'name','mobile','email','subject','created_date']

class amberpet_samithi_reportAdmin(admin.ModelAdmin):
    list_display=['id', 'samithi','name_of_the_activity','date_of_activity'
        ,'submitted_by','created_date']





# Register your models here.
admin.site.register(Report, ReportAdmin)
admin.site.register(Samathi)
admin.site.register(Samithi_office_bearers,Samithi_office_bearersAdmin)
admin.site.register(Dist_office_bearers,Dist_office_bearersAdmin)
admin.site.register(Sivam_Events,Sivam_EventsAdmin)
admin.site.register(About_HNR_Samithi,About_HNR_SamithiAdmin)
admin.site.register(Carousel)
admin.site.register(Landing_page)
admin.site.register(amberpet_samithi)
admin.site.register(amberpet_samithi_report,amberpet_samithi_reportAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Sivam_about_page)
admin.site.register(Sivam_spw_page)
admin.site.register(Sivam_ew_page)
admin.site.register(Sivam_srw_page)
admin.site.register(Seva_Report)
admin.site.register(samithi_login)

from django.urls import path
from sivam_app import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('sivam_history_form', views.sivam_history_form, name='sivam_history_form'),
    path('sivam_history_records', views.sivam_history_records, name='sivam_history_records'),
    path('update_sivam_history/<int:id>', views.update_sivam_history, name='update_sivam_history'),
    path('delete_sivam_history/<int:id>', views.delete_sivam_history, name='delete_sivam_history'),
    path('sivam', views.sivam, name='sivam'),
    path('samithis', views.samithis, name='samithis'),
    path('contact', views.contact, name='contact'),
    path('delete_func/<int:id>', views.delete_func, name='delete_func'),
    path('contact_form', views.contact_form, name='contact_form'),
    path('update_contact_form/<int:id>', views.update_contact_form, name='update_contact_form'),
    path('delete_contact/<int:id>', views.delete_contact, name='delete_contact'),
    path('contact_form_records', views.contact_form_records, name='contact_form_records'),
    path('change_password',views.change_password, name="change_password"),
    path('spiritual_wing_form',views.spiritual_wing_form, name="spiritual_wing_form"),

    path('spw_records',views.spw_records, name='spw_records'),
    path('update_spw/<int:id>',views.update_spw, name='update_spw'),
    path('delete_spw/<int:id>', views.delete_spw, name='delete_spw'),
    path('ew_form',views.ew_form, name="ew_form"),
    path('ew_records',views.ew_records, name='ew_records'),
    path('update_ew<int:id>', views.update_ew, name="update_ew"),
    path('delete_ew/<int:id>', views.delete_ew, name="delete_ew"),
    path('srw_form', views.srw_form, name="srw_form"),
    path('srw_records', views.srw_records, name="srw_records"),
    path('update_srw<int:id>', views.update_srw, name="update_srw"),
    path('delete_srw<int:id>', views.delete_srw, name="delete_srw"),
    path('spw_display_page', views.spw_display_page, name="spw_display_page"),
    path('ew_display_page', views.ew_display_page, name="ew_display_page"),
    path('srw_display_page', views.srw_display_page, name="srw_display_page"),


]

from django.urls import path
from accounts import views
# from .views import ReportListView
# from .views import render_pdf_view
# from .views import report_render_pdf_view
from django.views.generic import TemplateView
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('submit', views.submit, name='submit'),
    path('himayathnagar', views.himayathnagar, name='himayathnagar'),
    path('activity_himayathnagar/<int:id>', views.activity_himayathnagar, name='activity_himayathnagar'),
    path('total_records', views.total_records, name='total_records'),
    path('delete_func/<int:id>', views.delete_func, name='delete_func'),
    path('update_func/<int:id>', views.update_func, name='update_func'),
    path('search_total_records', views.search_total_records, name='search_total_records'),
    path('report_render_pdf_view/<pk>', views.report_render_pdf_view, name='report_render_pdf_view'),
    path('samithi_office_bearers', views.samithi_office_bearers, name='samithi_office_bearers'),
    path('about_samithi', views.about_samithi, name='about_samithi'),
    path('samithi_report', views.samithi_report, name='samithi_report'),
    path('update_samithi/<int:id>', views.update_samithi, name='update_samithi'),
    path('delete_samithi/<int:id>', views.delete_samithi, name='delete_samithi'),
    path('office_bearers_records', views.office_bearers_records, name='office_bearers_records'),
    path('update_office_bearers/<int:id>', views.update_office_bearers, name='update_office_bearers'),
    path('delete_office_bearers/<int:id>', views.delete_office_bearers, name='delete_office_bearers'),
    path('sivam_signup', views.sivam_signup, name='sivam_signup'),
    path('sivam_login', views.sivam_login, name='sivam_login'),
    path('sivam_dashboard', views.sivam_dashboard, name='sivam_dashboard'),
    path('landing_page_form', views.landing_page_form, name='landing_page_form'),
    path('slider_form', views.slider_form, name='slider_form'),
    path('slider_report_page', views.slider_report_page, name='slider_report_page'),
    path('update_slider/<int:id>', views.update_slider, name='update_slider'),
    path('delete_slider/<int:id>', views.delete_slider, name='delete_slider'),
    path('landing_page_report', views.landing_page_report, name='landing_page_report'),
    path('update_landing_page_form/<int:id>', views.update_landing_page_form, name='update_landing_page_form'),
    path('delete_landing_page_form/<int:id>', views.delete_landing_page_form, name='delete_landing_page_form'),
    path('sivam_events_form', views.sivam_events_form, name='sivam_events_form'),
    path('sivam_events_page', views.sivam_events_page, name='sivam_events_page'),
    path('sivam_event_page/<int:id>', views.sivam_event_page, name='sivam_event_page'),
    path('search_sivam_events', views.search_sivam_events, name='search_sivam_events'),
    path('s_event_update/<int:id>', views.s_event_update, name='s_event_update'),
    path('s_event_delete/<int:id>', views.s_event_delete, name='s_event_delete'),
    path('event_render_pdf_view/<pk>', views.event_render_pdf_view, name='event_render_pdf_view'),
    path('samithis_sign_up', views.samithis_sign_up, name='samithis_sign_up'),
    path('samithis_login', views.samithis_login, name='samithis_login'),
    path('seva_report_form', views.seva_report_form, name='seva_report_form'),
    path('samithi_report/<int:id>', views.samithi_report, name='samithi_report'),
    path('sivam_ob_form>', views.sivam_ob_form, name='sivam_ob_form'),
    path('sivam_ob_reports', views.sivam_ob_reports, name='sivam_ob_reports'),
    path('sivam_ob_update/<int:id>', views.sivam_ob_update, name='sivam_ob_update'),
    path('sivam_ob_delete/<int:id>', views.sivam_ob_delete, name='sivam_ob_delete'),




    # amberpet-samithi-urls:
    # path('as_signup', views.as_signup, name='as_signup'),
    # path('as_login/<int:id>', views.as_login, name='as_login'),
    path('as_dashboard/<int:id>', views.as_dashboard, name='as_dashboard'),
    path('as_form', views.as_form, name='as_form'),
    path('as_form_total_records', views.as_form_total_records, name='as_form_total_records'),
    path('as_update_record/<int:id>', views.as_update_record, name='as_update_record'),
    path('as_delete_record/<int:id>', views.as_delete_record, name='as_delete_record'),
    path('as_single_report_form', views.as_single_report_form, name='as_single_report_form'),
    path('as_total_reports', views.as_total_reports, name='as_total_reports'),
    path('as_search_records', views.as_search_records, name='as_search_records'),
    path('as_delete_report/<int:id>', views.as_delete_report, name='as_delete_report'),
    path('as_update_report/<int:id>', views.as_update_report, name='as_update_report'),
    path('as_report_pdf/<pk>', views.as_report_pdf, name='as_report_pdf'),
    path('as_ob_form>', views.as_ob_form, name='as_ob_form'),
    path('as_ob_total_records>', views.as_ob_total_records, name='as_ob_total_records'),
    path('as_update_ob/<int:id>', views.as_update_ob, name='as_update_ob'),
    path('as_delete_ob/<int:id>', views.as_delete_ob, name='as_delete_ob'),
    path('as_display_page/<int:id>', views.as_display_page, name='as_display_page'),
    path('as_report_display_page/<int:id>', views.as_report_display_page, name='as_report_display_page'),
    path('all_samithi_link_page', views.all_samithi_link_page, name='all_samithi_link_page'),




]

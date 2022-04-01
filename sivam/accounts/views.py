from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Report, Samathi,Samithi_office_bearers,Dist_office_bearers,\
    Sivam_Events,About_HNR_Samithi,Carousel,Landing_page,Sivam_Events,Dist_office_bearers,\
    amberpet_samithi,amberpet_samithi_report,as_office_bearers,Seva_Report,Signup_User,samithi_login
from accounts.forms import Samithi_office_bearersModelForm,\
Dist_office_bearersModelForm,Sivam_EventsModelForm,About_HNR_SamithiModelForm,\
    Landing_pageModelForm,CarouselModelForm,Sivam_EventsModelForm,Dist_office_bearersModelForm,\
    amberpet_samithiModelForm,amberpet_samithi_reportModelForm,as_office_bearersModelForm,\
    Seva_ReportModelForm

from django.db.models import Count
from sivam_app  import views
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse



# Create your views here.

# def signup (request):
#     if request.method == 'POST':
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'Username already exists!')
#                 return redirect('signup')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'Email already exists!')
#                 return redirect('signup')
#
#             else:
#                 user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,
#                 email=email, password=password1)
#                 user.save();
#                 Samathi.objects.create(user=user, samthi=request.POST['samithi'])
#                 print('user created')
#                 return redirect('login')
#
#         else:
#             messages.info(request,'Password do ot matching..')
#             return redirect('signup')
#         return redirect('/')
#     else:
#         return render(request,'accounts/signup.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['passwordagain']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html',{'error':'Username has Already been Teken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])\

                title = request.POST['title']
                extra_field = samithi_login(title=title, user=user)
                extra_field.save()
                auth.login(request, user)
                return HttpResponse("Signed Up!")
        else:
            return render(request, 'accounts/signup.html', {'error':"Passwords Don't Match"})
    else:
        return render(request, 'accounts/signup.html')





    # form = Register_UserModelForm
    # report_form = {'form': form, }
    #
    # if request.method == 'POST':
    #     form = Register_UserModelForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         messages.success(request, ('Something went wrong try again...'))
    #         return redirect('signup')
    #
    #     messages.success(request, ('Your report has been submitted successfully!'))
    #     return redirect('as_dashboard')
    # else:
    #     return render(request, 'accounts/signup.html', report_form)



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
            # return HttpResponse('Logged In !')
        else:
            messages.info(request, ' Invalid credentials')
            return redirect('login')

    else:
        return render (request, 'accounts/login.html')



@login_required(login_url='/login/')
def dashboard(request):
    swd = samithi_login.objects.filter(user = request.user)
    # request.session.samithi = swd[0].samithi
    data = {'swd':swd,}
    return render (request, 'accounts/dashboard.html', data)


def submit(request):
    form = ReportModelForm
    report_form = {'form':form,}

    if request.method == 'POST':
        form = ReportModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request,('Something went wrong try again...'))
            return redirect('submit')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect ('dashboard')
    else:
        return render(request, 'accounts/submit.html',report_form)


def himayathnagar(request):
    about_samithi = About_HNR_Samithi.objects.all()
    office_bearers = Samithi_office_bearers.objects.all()
    recent_reports = Report.objects.all().order_by('-id')[:4]


    data = {'recent_reports': recent_reports, 'office_bearers':office_bearers,
            'about_samithi':about_samithi,}
    return render(request, 'accounts/himayathnagar.html', data)


def activity_himayathnagar (request, id):
    all_reports = Report.objects.filter(id=id)
    data = {'all_reports': all_reports,
            }
    return render (request, 'accounts/activity_himayathnagar.html', data)

def total_records(request):

    rep = Report.objects.all().order_by('-created_date')
    paginator = Paginator(rep, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'accounts/total_records.html', data)

def delete_func(request, id):
    activity = Report.objects.get(id=id)
    activity.delete()
    return redirect('total_records')

def update_func(request, id):
    activity = Report.objects.get(id=id)
    form = ReportModelForm (instance=activity)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = ReportModelForm(request.POST, request.FILES,instance=activity,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('update_report_form.html')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('dashboard')
    else:
        return render(request, 'accounts/update_report_form.html', report_form)

def search_total_records(request):
    search_records = Report.objects.all().order_by('created_date')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            search_records = search_records.filter( Q(write_up__icontains=keyword) | Q(date_of_activity__icontains=keyword) | Q(name_of_the_activity__icontains=keyword))

    paginator = Paginator(search_records, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'search_records':page_obj.object_list,
            'paginator': paginator,
            'page_number': int(page_number),
            }
    return render(request, 'accounts/search_total_records.html', data)

def report_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    report = get_object_or_404(Report, pk=pk)
    template_path = 'accounts/pdf2.html'
    context = {'report': report,}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    # response['Content-Disposition'] = 'attachment; filename="service-report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="service-report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def samithi_office_bearers (request):
    form = Samithi_office_bearersModelForm
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Samithi_office_bearersModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('samithi_office_bearers')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('dashboard')
    else:
        return render(request, 'accounts/samithi_office_bearers.html', report_form)


def about_samithi(request):
    form = About_HNR_SamithiModelForm
    report_form = {'form': form, }

    if request.method == 'POST':
        form = About_HNR_SamithiModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('samithi_office_bearers')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('dashboard')
    else:
        return render(request, 'accounts/about_samithi.html', report_form)


def office_bearers_records(request):
    rep = Samithi_office_bearers.objects.all().order_by('-created_date')
    paginator = Paginator(rep, per_page=10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'accounts/office_bearers_records.html', data)

def update_office_bearers(request, id):
    ob = Samithi_office_bearers.objects.get(id=id)
    form = Samithi_office_bearersModelForm (instance=ob)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Samithi_office_bearersModelForm(request.POST, request.FILES,instance=ob,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('update_office_bearers')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('dashboard')
    else:
        return render(request, 'accounts/update_office_bearers.html', report_form)


def samithi_report(request):
    rep = About_HNR_Samithi.objects.all()
    paginator = Paginator(rep, per_page=10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'accounts/samithi_report.html', data)


def delete_office_bearers(request, id):
    activity = Samithi_office_bearers.objects.get(id=id)
    activity.delete()
    return redirect('office_bearers_records')

def update_samithi(request,id):
    uob = About_HNR_Samithi.objects.get(id=id)
    form = About_HNR_SamithiModelForm(instance=uob)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = About_HNR_SamithiModelForm(request.POST,request.FILES,instance=uob )
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('update_samithi')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('dashboard')
    else:
        return render(request, 'accounts/update_samithi.html', report_form)

def delete_samithi(request, id):
    activity = About_HNR_Samithi.objects.get(id=id)
    activity.delete()
    return redirect('samithi_report')

def sivam_signup (request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists!')
                return redirect('signup')

            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,
                email=email, password=password1)
                user.save();
                Samathi.objects.create(user=user, samthi=request.POST['samithi'])
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'Password do ot matching..')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request,'accounts/sivam_signup.html')


def sivam_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('sivam_dashboard')
        else:
            messages.info(request, ' Invalid credentials')
            return redirect('sivam_login')

    else:
        return render (request, 'accounts/sivam_login.html')

def sivam_dashboard(request):
    return render (request, 'accounts/sivam_dashboard.html')


def landing_page_form(request):
    form = Landing_pageModelForm
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Landing_pageModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('landing_page_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'accounts/landing_page_form.html', report_form)


def slider_form(request):
    form = CarouselModelForm
    report_form = {'form': form,}

    if request.method == 'POST':
        form = CarouselModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('slider_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'accounts/slider_form.html', report_form)


def landing_page_report(request):
    rep = Landing_page.objects.all()
    paginator = Paginator(rep, per_page=10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'accounts/landing_page_report.html', data)

def update_landing_page_form(request,id):
    update_form = Landing_page.objects.get(id=id)
    form = Landing_pageModelForm (instance=update_form)

    report_form = {'form': form, }

    if request.method == 'POST':
        form = Landing_pageModelForm(request.POST, request.FILES,instance=update_form )
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('update_landing_page_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'accounts/update_landing_page_form.html', report_form)


def delete_landing_page_form(request, id):
    delete_form = Landing_page.objects.get(id=id)
    delete_form.delete()
    return redirect('landing_page_report')


def slider_report_page(request):
    rep = Carousel.objects.all()
    paginator = Paginator(rep, per_page=10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'accounts/slider_report_page.html', data)

def update_slider(request,id):
    update_form = Carousel.objects.get(id=id)
    form = CarouselModelForm (instance=update_form)

    report_form = {'form': form, }

    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES,instance=update_form )
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('update_slider')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'accounts/update_slider.html', report_form)


def delete_slider(request, id):
    delete_form = Carousel.objects.get(id=id)
    delete_form.delete()
    return redirect('slider_report_page')


def sivam_events_form(request):
    form = Sivam_EventsModelForm
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Sivam_EventsModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('sivam_events_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'accounts/sivam_events_form.html', report_form)



def sivam_events_page(request):
    rep = Sivam_Events.objects.all()
    paginator = Paginator(rep, per_page=10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'accounts/sivam_events_page.html', data)

def search_sivam_events(request):
    search_records = Sivam_Events.objects.all().order_by('date_of_activity')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            search_records = search_records.filter( Q(write_up__icontains=keyword) | Q(date_of_activity__icontains=keyword) | Q(name_of_the_activity__icontains=keyword))

    paginator = Paginator(search_records, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'search_records':page_obj.object_list,
            'paginator': paginator,
            'page_number': int(page_number),
            }
    return render(request, 'accounts/search_sivam_events.html', data)

def s_event_delete(request, id):
    activity = Sivam_Events.objects.get(id=id)
    activity.delete()
    return redirect('sivam_events_page')

def s_event_update(request, id):
    activity = Sivam_Events.objects.get(id=id)
    form = Sivam_EventsModelForm (instance=activity)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Sivam_EventsModelForm(request.POST, request.FILES,instance=activity,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('s_event_update.html')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'accounts/s_event_update.html', report_form)

def event_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    report = get_object_or_404(Sivam_Events, pk=pk)
    template_path = 'accounts/sivam_event_pdf.html'
    context = {'report': report,}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    # response['Content-Disposition'] = 'attachment; filename="service-report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="Sivam-Event.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def sivam_event_page(request,id):
    all_reports = Sivam_Events.objects.get(id=id)
    data = {'all_reports': all_reports,}
    return render(request, 'accounts/sivam_event_page.html', data)

def samithis_sign_up(request):
    return render(request, 'accounts/samithis_sign_up.html' )

def samithis_login(request):
    about_samithi = amberpet_samithi.objects.all()
    data = {'about_samithi':about_samithi,}
    return render(request, 'accounts/samithis_login.html',data )

# AMBERPET SAMITHI VIEWS START

# def as_signup (request):
#     if request.method == 'POST':
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'Username already exists!')
#                 return redirect('as_signup')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'Email already exists!')
#                 return redirect('as_signup')
#
#             else:
#                 user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,
#                 email=email, password=password1)
#                 user.save();
#                 print('user created')
#                 return redirect('as_login')
#     else:
#         return render(request, 'accounts/amberpet/as_signup.html')

# def as_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username, password=password)
#
#         if user is not None:
#             auth.login(request, user)
#             return HttpResponse('Logged In !')
#         else:
#             messages.info(request, ' Invalid credentials')
#             return redirect('login')
#
#     else:
#         return render(request, 'accounts/as_login.html')
# def as_login(request,id):
#     about_samithi = amberpet_samithi.objects.get(id=id)
#     data = {'about_samithi': about_samithi,}
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username, password=password)
#
#         if user is not None:
#             auth.login(request, user)
#             return redirect('as_dashboard')
#         else:
#             messages.info(request, ' Invalid credentials')
#             return redirect('as_login')
#
#     else:
#         return render (request, 'accounts/amberpet/as_login.html',data)



def as_dashboard(request,id):
    about_samithi = amberpet_samithi.objects.get(id=id)
    recent_reports = amberpet_samithi_report.objects.filter(samithi__iexact=about_samithi.samithi)
    data = {'about_samithi':about_samithi, 'recent_reports':recent_reports}
    return render (request, 'accounts/amberpet/as_dashboard.html',data)


def as_form(request):
    form = amberpet_samithiModelForm
    report_form = {'form': form, }

    if request.method == 'POST':
        form = amberpet_samithiModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('as_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('as_dashboard')
    else:
        return render(request, 'accounts/amberpet/as_form.html', report_form)

def as_form_total_records(request):
    rep = amberpet_samithi.objects.filter(samithi__iexact=samithi_login.objects.filter(user=request.user)[0].title)
    paginator = Paginator(rep, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'accounts/amberpet/as_form_total_records.html', data)

def as_update_record(request, id):
    activity = amberpet_samithi.objects.get(id=id)
    form = amberpet_samithiModelForm (instance=activity)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = amberpet_samithiModelForm(request.POST, request.FILES,instance=activity,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('as_update_record')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('dashboard')
    else:
        return render(request, 'accounts/amberpet/as_update_record.html', report_form)

def as_delete_record(request, id):
    activity = amberpet_samithi.objects.get(id=id)
    activity.delete()
    return redirect('as_form_total_records')

def as_single_report_form(request):
    form = amberpet_samithi_reportModelForm
    report_form = {'form':form,}

    if request.method == 'POST':
        form = amberpet_samithi_reportModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request,('Something went wrong try again...'))
            return redirect('as_single_report_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect ('dashboard')
    else:
        return render(request, 'accounts/amberpet/as_single_report_form.html',report_form)

def as_total_reports(request):
    rep = amberpet_samithi_report.objects.filter(samithi__iexact=samithi_login.objects.filter(user=request.user)[0].title)
    paginator = Paginator(rep, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'accounts/amberpet/as_total_reports.html', data)

def as_search_records(request):
    search_records = amberpet_samithi_report.objects.filter(samithi__iexact=samithi_login.objects.filter(user=request.user)[0].title)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            search_records = search_records.filter( Q(write_up__icontains=keyword) | Q(date_of_activity__icontains=keyword) | Q(name_of_the_activity__icontains=keyword))

    paginator = Paginator(search_records, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'search_records':page_obj.object_list,
            'paginator': paginator,
            'page_number': int(page_number),
            }
    return render(request, 'accounts/amberpet/as_search_records.html', data)


def as_delete_report(request, id):
    activity = amberpet_samithi_report.objects.get(id=id)
    activity.delete()
    return redirect('as_total_reports')

def as_update_report(request, id):
    activity = amberpet_samithi_report.objects.get(id=id)
    form = amberpet_samithi_reportModelForm (instance=activity)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = amberpet_samithi_reportModelForm(request.POST, request.FILES,instance=activity,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('as_update_report')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('dashboard')
    else:
        return render(request, 'accounts/amberpet/as_update_report.html', report_form)

def as_report_pdf(request, *args, **kwargs):
    pk = kwargs.get('pk')
    report = get_object_or_404(amberpet_samithi_report, pk=pk)
    template_path = 'accounts/amberpet/as_report_pdf.html'
    context = {'report': report,}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    # response['Content-Disposition'] = 'attachment; filename="service-report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def as_ob_form (request):
    form = as_office_bearersModelForm
    report_form = {'form': form, }

    if request.method == 'POST':
        form = as_office_bearersModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('as_ob_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('dashboard')
    else:
        return render(request, 'accounts/amberpet/as_ob_form.html', report_form)

def as_ob_total_records(request):
    rep = as_office_bearers.objects.filter(samithi__iexact=samithi_login.objects.filter(user=request.user)[0].title)
    paginator = Paginator(rep, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'accounts/amberpet/as_ob_total_records.html', data)

def as_update_ob(request, id):
    ob = as_office_bearers.objects.get(id=id)
    form = as_office_bearersModelForm (instance=ob)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = as_office_bearersModelForm(request.POST, request.FILES,instance=ob,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('as_update_ob')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('dashboard')
    else:
        return render(request, 'accounts/amberpet/as_update_ob.html', report_form)



def as_delete_ob(request, id):
    activity = as_office_bearers.objects.get(id=id)
    activity.delete()
    return redirect('as_ob_total_records')

def as_display_page(request,id):
    about_samithi = amberpet_samithi.objects.get(id=id)
    office_bearers = as_office_bearers.objects.filter(samithi__iexact= about_samithi.samithi)
    recent_reports = amberpet_samithi_report.objects.filter(samithi__iexact= about_samithi.samithi).order_by('-id')[:4]

    data = {'recent_reports': recent_reports, 'office_bearers':office_bearers,
            'about_samithi':about_samithi,}
    return render(request, 'accounts/amberpet/as_display_page_final.html', data)

def all_samithi_link_page(request):
    about_samithi = amberpet_samithi.objects.all()
    samithi = {'about_samithi':about_samithi,}
    return render(request, 'accounts/amberpet/all_samithi_link_page.html',samithi)

def as_report_display_page (request, id):
    all_reports = amberpet_samithi_report.objects.get(id=id)
    data = {'all_reports': all_reports,}
    return render (request, 'accounts/amberpet/as_report_display_page.html', data)

def seva_report_form(request):
    form = Seva_ReportModelForm
    report_form = {'form': form, }
    if request.method == 'POST':
        form = Seva_ReportModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('seva_report_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('as_dashboard')
    else:
        return render(request, 'accounts/amberpet/seva_report_form.html', report_form)


def sivam_ob_form (request):
    form = Dist_office_bearersModelForm
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Dist_office_bearersModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('sivam_ob_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'accounts/sivam_ob_form.html', report_form)

def sivam_ob_reports(request):
    rep = Dist_office_bearers.objects.all().order_by('-id')
    paginator = Paginator(rep, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'accounts/sivam_ob_reports.html', data)

def sivam_ob_update(request, id):
    ob = Dist_office_bearers.objects.get(id=id)
    form = Dist_office_bearersModelForm (instance=ob)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Dist_office_bearersModelForm(request.POST, request.FILES,instance=ob,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('sivam_ob_update')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'accounts/sivam_ob_update.html', report_form)



def sivam_ob_delete(request, id):
    activity = Dist_office_bearers.objects.get(id=id)
    activity.delete()
    return redirect('sivam_ob_records')

# def signup(request):
#     error = False
#     if request.method == 'POST':
#         f = request.POST['fname']
#         l = request.POST['lname']
#         u = request.POST['uname']
#
#         p = request.POST['pwd']
#         e = request.POST['email']
#
#         con = request.POST['contact']
#         s = request.POST['samithi']
#         user = User.objects.create_user(email=e,username=u, password=p, first_name=f,last_name=l)
#         sign = Signup_User.objects.create(samithi=samithi,user=user,mobile=con,)
#         if reg == "Doctor":
#             status = Doc_Status.objects.get(status="Active")
#             pat = Doctor.objects.create(sign=sign,status=status)
#         else:
#             doc = Patient.objects.create(sign=sign)
#         error = True
#     d = {'error':error}
#     return render(request, 'accounts/signup.html',d)
#












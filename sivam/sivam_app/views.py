from django.shortcuts import render, redirect
from accounts.models import Report, Samathi
from accounts.models import Carousel,Landing_page,Sivam_Events,\
    Dist_office_bearers,Contact, Sivam_about_page,\
    Sivam_spw_page,Sivam_ew_page,Sivam_srw_page,amberpet_samithi
from accounts.forms import Dist_office_bearersModelForm,Sivam_spw_pageModelForm,\
    Sivam_ew_pageModelForm,Sivam_srw_pageModelForm
from django.contrib import messages
from django.core.paginator import Paginator
from accounts.forms import Sivam_about_pageModelForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    carousel = Carousel.objects.all()
    fpage = Landing_page.objects.all()
    about_samithi = amberpet_samithi.objects.all()
    events = Sivam_Events.objects.all().order_by('-id')[:4]

    context = {
        'carousel': carousel, 'fpage':fpage, 'events':events,
        'about_samithi':about_samithi,
    }
    return render (request, 'sivam_app/index.html',context)


def sivam_history_form(request):
    form = Sivam_about_pageModelForm
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Sivam_about_pageModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('sivam_history_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'sivam_app/sivam_history_form.html', report_form)

def sivam_history_records(request):

    rep = Sivam_about_page.objects.all().order_by('-created_date')
    paginator = Paginator(rep, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'sivam_app/sivam_history_records.html', data)

def delete_sivam_history(request, id):
    activity = Sivam_about_page.objects.get(id=id)
    activity.delete()
    return redirect('sivam_history_records')

def update_sivam_history(request, id):
    activity = Sivam_about_page.objects.get(id=id)
    form = Sivam_about_pageModelForm (instance=activity)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Sivam_about_pageModelForm(request.POST, request.FILES,instance=activity,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('update_sivam_history.html')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'sivam_app/update_sivam_history.html', report_form)


def spiritual_wing_form(request):
    form = Sivam_spw_pageModelForm
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Sivam_spw_pageModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('spiritual_wing_form')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'sivam_app/spiritual_wing_form.html', report_form)



def spw_records(request):
    rep = Sivam_spw_page.objects.all().order_by('-created_date')
    paginator = Paginator(rep, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep': page_obj.object_list,
            'paginator': paginator,
            'page_number': int(page_number),
            }

    return render(request, 'sivam_app/spw_records.html', data)

def delete_spw(request, id):
    activity = Sivam_spw_page.objects.get(id=id)
    activity.delete()
    return redirect('spw_records')

def update_spw(request, id):
    activity = Sivam_spw_page.objects.get(id=id)
    form = Sivam_spw_pageModelForm (instance=activity)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Sivam_spw_pageModelForm(request.POST, request.FILES,instance=activity,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('update_spw.html')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('dashboard')
    else:
        return render(request, 'sivam_app/update_spw.html', report_form)

def ew_form(request):
    form = Sivam_ew_pageModelForm
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Sivam_ew_pageModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('ew_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'sivam_app/ew_form.html', report_form)

def ew_records(request):

    rep = Sivam_ew_page.objects.all().order_by('-created_date')
    paginator = Paginator(rep, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'sivam_app/ew_records.html', data)

def delete_ew(request, id):
    activity = Sivam_ew_page.objects.get(id=id)
    activity.delete()
    return redirect('spw_records')

def update_ew(request, id):
    activity = Sivam_ew_page.objects.get(id=id)
    form = Sivam_ew_pageModelForm (instance=activity)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Sivam_ew_pageModelForm(request.POST, request.FILES,instance=activity,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('update_ew.html')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'sivam_app/update_ew.html', report_form)

def srw_form(request):
    form = Sivam_srw_pageModelForm
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Sivam_srw_pageModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('srw_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'sivam_app/srw_form.html', report_form)

def srw_records(request):
    rep = Sivam_srw_page.objects.all().order_by('-created_date')
    paginator = Paginator(rep, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'sivam_app/srw_records.html', data)

def delete_srw(request, id):
    activity = Sivam_srw_page.objects.get(id=id)
    activity.delete()
    return redirect('srw_records')

def update_srw(request, id):
    activity = Sivam_srw_page.objects.get(id=id)
    form = Sivam_srw_pageModelForm (instance=activity)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Sivam_srw_pageModelForm(request.POST, request.FILES,instance=activity,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('update_srw.html')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'sivam_app/update_srw.html', report_form)

def sivam(request):
    sivam_history = Sivam_about_page.objects.all()
    data = {'sivam_history':sivam_history,}
    return render(request, 'sivam_app/sivam.html',data)

def spw_display_page(request):
    spw = Sivam_spw_page.objects.all()
    data = {'spw':spw,}
    return render(request, 'sivam_app/spw_display_page.html',data)

def ew_display_page(request):
    ew = Sivam_ew_page.objects.all()
    data = {'ew':ew,}
    return render(request, 'sivam_app/ew_display_page.html',data)

def srw_display_page(request):
    srw = Sivam_srw_page.objects.all()
    data = {'srw':srw,}
    return render(request, 'sivam_app/srw_display_page.html',data)


def samithis(request):
    return render (request, 'sivam_app/samithis.html')



def submitform(request):
    return render (request,'sivam_app/submit.html')




def delete_func(request, id):
    activity = Report.objects.filter(id=id)
    activity.delete()
    return redirect('total_records')

def contact_form(request):
    # contact = Contact.objects.all().order_by('created_date')

    form = Dist_office_bearersModelForm
    report_form = {'form': form, }
    if request.method == 'POST':
        form = Dist_office_bearersModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('contact_form')

        messages.success(request, ('Your report has been submitted successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'sivam_app/contact_form.html', report_form)

def contact(request):
    sob = Dist_office_bearers.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        write_up = request.POST.get('write_up')
        contact = Contact(
            name = name,
            email = email,
            mobile = mobile,
            subject = subject,
            write_up = write_up,)

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email
        # send_mail(
        #     'Sivam Mail',
        #     'Devotee Message.',
        #     'mnagendarr@gmail.com',
        #     ['admin_email'],
        #     fail_silently=False,)
        contact.save()
        messages.success(request, 'Contact request submitted successfully')
        return redirect('contact')
    data = {'sob':sob,}
    return render(request,'sivam_app/contact.html',data)

def contact_form_records(request):

    rep = Dist_office_bearers.objects.all().order_by('-created_date')
    paginator = Paginator(rep, per_page=5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {'rep':page_obj.object_list,
            'paginator':paginator,
            'page_number': int(page_number),
            }
    return render (request,'sivam_app/contact_form_records.html', data)

def update_contact_form(request, id):
    activity = Dist_office_bearers.objects.get(id=id)
    form = Dist_office_bearersModelForm (instance=activity)
    report_form = {'form': form, }

    if request.method == 'POST':
        form = Dist_office_bearersModelForm(request.POST, request.FILES,instance=activity,)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('Something went wrong try again...'))
            return redirect('update_contact_form.html')

        messages.success(request, ('Your report has been updated successfully!'))
        return redirect('sivam_dashboard')
    else:
        return render(request, 'sivam_app/update_contact_form.html', report_form)

def delete_contact(request, id):
    activity = Dist_office_bearers.objects.get(id=id)
    activity.delete()
    return redirect('contact_form_records')

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = request.user
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"

    return render(request,'sivam_app/change_password.html',locals())

def spw_form(request):
    pass
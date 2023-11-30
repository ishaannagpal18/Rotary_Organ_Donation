from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import *
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import uuid

def home(request):
    return render(request, 'index.html')

def organ_donation(request):
    return render(request, 'organ_donation.html')

def organ_transplantation(request):
    return render(request, 'organ_transplantation.html')

def organ_donation_in_india(request):
    return render(request, 'organ_donation_in_india.html')

def why_donate(request):
    return render(request, 'why_donate.html')

def living_donation(request):
    return render(request, 'living_donation.html')

def how_to_become_a_donor(request):
    return render(request, 'how_to_become_a_donor.html')

def myths_vs_facts(request):
    return render(request, 'myths_vs_facts.html')

def awareness_lightening_up_light(request):
    return render(request, 'awareness_lightening_up_light.html')

def tho_act(request):
    return render(request, 'tho_act.html')

def all_religion_support_organ_donation(request):
    return render(request, 'all_religion_support_organ_donation.html')

def faqs(request):
    return render(request, 'faqs.html')

def about_rotary(request):
    return render(request, 'about_rotary.html')

def news(request):
    return render(request, 'news.html')

def events(request):
    return render(request, 'events.html')

def our_inspirations(request):
    return render(request, 'our_inspiration.html')

def contact(request):
    return render(request, 'contact.html')


def pledge_now(request):

    if request.method == 'POST' and request.FILES['sign'] and request.FILES['witness1_sign'] and request.FILES['witness2_sign']:
        heart = False
        lungs = False
        kidneys = False
        liver = False
        pancreas = False
        all_organs = False
        corneas_or_eye_balls = False
        skin = False
        bones = False
        heart_valves = False
        blood_vessels = False
        all_tissues = False
        reg_number = request.POST.get('reg_number')
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        resident = request.POST.get('resident')
        heart = request.POST.get('heart')
        lungs = request.POST.get('lungs')
        kidneys = request.POST.get('kidneys')
        liver = request.POST.get('liver')
        pancreas = request.POST.get('pancreas')
        any_other_organ = request.POST.get('any_other_organ')
        all_organs = request.POST.get('all_organs')
        blood_group = request.POST.get('blood_group')
        gender = request.POST.get('gender')
        corneas_or_eye_balls = request.POST.get('corneas_or_eye_balls')
        skin = request.POST.get('skin')
        bones = request.POST.get('bones')
        heart_valves = request.POST.get('heart_valves')
        blood_vessels = request.POST.get('blood_vessels')
        any_other_tissue = request.POST.get('any_other_tissue')
        all_tissues = request.POST.get('all_tissues')
        sign=request.FILES.get('sign')
        address = request.POST.get('address')
        tel_no = request.POST.get('tel_no')
        email = request.POST.get('email')
        date = request.POST.get('date')
        witness1_sign=request.FILES.get('witness1_sign')
        witness1_name = request.POST.get('witness1_name')
        witness1_age = request.POST.get('witness1_age')
        witness1_dob = request.POST.get('witness1_dob')
        witness1_resident = request.POST.get('witness1_resident')
        witness1_tel_no = request.POST.get('witness1_tel_no')
        witness1_email = request.POST.get('witness1_email')
        witness1_relation = request.POST.get('witness1_relation')
        witness2_sign=request.FILES.get('witness2_sign')
        witness2_name = request.POST.get('witness2_name')
        witness2_age = request.POST.get('witness2_age')
        witness2_dob = request.POST.get('witness2_dob')
        witness2_resident = request.POST.get('witness2_resident')
        witness2_tel_no = request.POST.get('witness2_tel_no')
        witness2_email = request.POST.get('witness2_email')
        witness2_relation = request.POST.get('witness2_relation')
        witness_dated = request.POST.get('witness_dated')
        witness_place = request.POST.get('witness_place')
        auth_token = str(uuid.uuid4())[:8]




        pledge_obj = Pledge.objects.create(reg_number=reg_number,auth_token=auth_token, name=name, age=age, dob=dob, resident=resident, heart=heart, lungs=lungs, kidneys=kidneys,liver=liver, pancreas=pancreas, any_other_organ=any_other_organ,all_organs=all_organs,blood_group=blood_group,gender=gender,corneas_or_eye_balls=corneas_or_eye_balls,skin=skin,bones=bones,heart_valves=heart_valves,blood_vessels=blood_vessels,any_other_tissue=any_other_tissue,all_tissues=all_tissues,sign=sign,address=address,tel_no=tel_no,email=email,date=date,witness1_sign=witness1_sign,witness1_name=witness1_name,witness1_age=witness1_age,witness1_dob=witness1_dob,witness1_resident=witness1_resident,witness1_tel_no=witness1_tel_no,witness1_email=witness1_email,witness1_relation=witness1_relation,witness2_sign=witness2_sign,witness2_name=witness2_name,witness2_age=witness2_age,witness2_dob=witness2_dob,witness2_resident=witness2_resident,witness2_tel_no=witness2_tel_no,witness2_email=witness2_email,witness2_relation=witness2_relation,witness_dated=witness_dated,witness_place=witness_place)
        pledge_obj.save()
        messages.success(request, 'Submitted Sucessfully')

        html_template = render_to_string('pledge_email.html', {'name':name, 'auth_token':auth_token})
        recipient_list = [email]
        message = EmailMessage('Pledge Number Generated', html_template,
                                   'ROTARY ORGAN DONATION <info@rotaryorgandonation.org>', [email])
        message.content_subtype = 'html'
        message.send()

        return HttpResponseRedirect(reverse('home'))

    return render(request, 'pledge_now.html')

def login(request):
    if request.method == 'POST':
        auth_token = request.POST.get('unique_id')
        user_id = Pledge.objects.filter(auth_token = auth_token).first()



        if user_id :
            if user_id.is_verified:
                messages.success(request,"Pledge Number Is Verified!")

                return HttpResponseRedirect(reverse('donor_card'))
            else:
                messages.success(request,"Pledge Number Isn't Verified Yet!")
                return HttpResponseRedirect(reverse('login'))
        else:
            messages.success(request,"Pledge Number Didn't Matched!")
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'login.html')

def donor_card(request):
    auth_token = request.GET.get('unique_id')
    user_id = Pledge.objects.filter(auth_token = auth_token).first()



    return render(request, 'donor_card.html', {'user_id':user_id})

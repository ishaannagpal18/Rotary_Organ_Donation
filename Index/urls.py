from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('organ-donation',views.organ_donation,name='organ_donation'),
    path('organ-translantation',views.organ_transplantation,name='organ_transplantation'),
    path('organ-donation-in-india',views.organ_donation_in_india,name='organ_donation_in_india'),
    path('why-donate',views.why_donate,name='why_donate'),
    path('living-donation',views.living_donation,name='living_donation'),
    path('how-to-become-a-donor',views.how_to_become_a_donor,name='how_to_become_a_donor'),
    path('myths-vs-facts',views.myths_vs_facts,name='myths_vs_facts'),
    path('awareness/lightening-up-light',views.awareness_lightening_up_light,name='awareness_lightening_up_light'),
    path('THO-act',views.tho_act,name='tho_act'),
    path('all-religion-support-organ-donation',views.all_religion_support_organ_donation,name='all_religion_support_organ_donation'),
    path('FAQs',views.faqs,name='faqs'),
    path('about-rotary',views.about_rotary,name='about_rotary'),
    path('news',views.news,name='news'),
    path('events',views.events,name='events'),
    path('our-inspirations',views.our_inspirations,name='our_inspirations'),
    path('contact-us',views.contact,name='contact'),
    path('pledge-now',views.pledge_now,name='pledge_now'),
    path('two-step-verification',views.login,name='login'),
    path('donor-card',views.donor_card,name='donor_card'),
]

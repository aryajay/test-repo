from django.conf.urls import url
from urlsapp import views

urlpatterns=[
    url(r'^hydjobs/',views.hydjobsinfo),
    url(r'^banjobs/',views.banjobsinfo),
    url(r'^chejobs/',views.chejobsinfo),
    url(r'^punjobs/',views.punjobsinfo),


]
from django.conf.urls import url
from urls import views
urlpatterns=[
    url(r'^hydjobs/',view.hydjobsinfo),
]
"""twoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import pa
from django.conf.urls import url
from django.contrib import admin
import django.views.defaults
from app1 import views as v1
from app2 import views as v2

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^mohan/',views.v1.wish1),
    url(r'^pradeep/',views.v2.wish2),
    url(r'^404/$', django.views.defaults.page_not_found, ),
]

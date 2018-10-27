from django.contrib import admin
from testapp.models import Hydjobs
admin.site.register(Hydjobs,HydjobsAdmin)
class HybjobsAdmin(Admin.ModelAdmin):
    list=['date','company','title','eligibility','address','email','phonenumber']


# Register your models
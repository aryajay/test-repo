from django.contrib import admin

from testapp.models import Hydjobs

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Hydjobs,HydjobsAdmin)


# Register your models here.

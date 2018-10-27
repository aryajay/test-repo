from django.contrib import admin
from data.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']
    admin.site.register(Employee.EmployeeAdmin)
# Register your models here.

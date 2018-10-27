from django.contrib import admin
from testapps.models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['rdate','moviename','hero','heroine','rating']
admin.site.register(Movie,MovieAdmin)


# Register your models here.

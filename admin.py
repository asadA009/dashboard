from django.contrib import admin
from .models import confrence


@admin.register(confrence)
class confrenceAdmin(admin.ModelAdmin):
    list_display=['id','confrence_ID','date','venu','image','confrence_Overview','registration','travel_information']

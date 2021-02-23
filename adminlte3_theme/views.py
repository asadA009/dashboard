from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from .models import confrence
from .seriliazers import confrenceSerializer
from rest_framework.renderers import JSONRenderer

#from rest_framework import viewsets

def conf_list(request):
    stu=confrence.objects.all()
    print(stu)
    #stu=confrence.objects.all()
    serializer=confrenceSerializer(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')



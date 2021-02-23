from rest_framework import serializers
from .models import confrence
from ckeditor.fields import RichTextField

class confrenceSerializer(serializers.Serializer):
    confrence_ID=serializers.CharField(max_length=20,default='')
    date=serializers.DateTimeField()
    venu=serializers.CharField(max_length=50, default='')
    image=serializers.ImageField() 
    confrence_Overview=RichTextField(blank=False,null=False)
    registration=RichTextField(blank=False,null=False)   
    travel_information=RichTextField(blank=False,null=False)  


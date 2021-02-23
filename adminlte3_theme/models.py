from django.db import models
from ckeditor.fields import RichTextField

class confrence(models.Model):
    id =models.AutoField
    confrence_ID=models.CharField(max_length=20,default='')
    date=models.DateTimeField(auto_now_add=False)
    venu=models.CharField(max_length=50, default='')
    image=models.ImageField(upload_to="admin-lte/images",default='')
    confrence_Overview=RichTextField(blank=False,null=False)
    registration=RichTextField(blank=False,null=False)
    travel_information=RichTextField(blank=False,null=False)

    def __str__(self):
        return self.confrence_ID
        

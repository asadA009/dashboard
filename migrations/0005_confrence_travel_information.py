# Generated by Django 3.1.6 on 2021-02-15 11:51

import ckeditor.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte3', '0004_auto_20210215_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='confrence',
            name='travel_information',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

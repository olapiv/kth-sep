# Generated by Django 2.2.6 on 2019-10-01 14:04

from django.db import migrations, models
from django.contrib.auth.models import Group, Permission

customer_service_officer = Group.objects.get_or_create(name='customer_service_officer')[0]
senior_customer_service_officer = Group.objects.get_or_create(name='senior_customer_service_officer')[0]
financial_manager = Group.objects.get_or_create(name='financial_manager')[0]
administration_manager = Group.objects.get_or_create(name='administration_manager')[0]
hr_manager = Group.objects.get_or_create(name='hr_manager')[0]

add_event_request_application = Permission.objects.get(codename='add_eventrequestapplication')

customer_service_officer.permissions.add(add_event_request_application)

class Migration(migrations.Migration):

    dependencies = [
        ('sep', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventrequestapplication',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('approved_by_scs', 'approved_by_scs')], default='created', max_length=50),
        ),
    ]
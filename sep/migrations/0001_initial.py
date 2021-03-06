# Generated by Django 2.2.6 on 2019-10-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventRequestApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('event_type', models.CharField(max_length=255)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('expected_number_of_attendees', models.IntegerField()),
                ('expected_budget', models.IntegerField()),
                ('status', models.CharField(choices=[('created', 'created'), ('approved_by_scs', 'approved_by_scs')], default='created', max_length=255)),
            ],
        ),
    ]

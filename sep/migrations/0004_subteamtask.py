# Generated by Django 2.2.6 on 2019-10-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sep', '0003_eventrequestapplication_event_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubteamTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('todo', 'todo'), ('in_progress', 'in_progress'), ('done', 'done')], default='todo', max_length=50)),
            ],
        ),
    ]
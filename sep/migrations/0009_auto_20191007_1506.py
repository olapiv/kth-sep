# Generated by Django 2.2.6 on 2019-10-07 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sep', '0008_subteamtask_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrabudgetrequest',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='extra_budget_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='staffrequest',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]

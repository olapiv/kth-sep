from django.db import models
from django.conf import settings


class EventRequestApplication(models.Model):
    event_name = models.CharField(max_length=255, default='')
    client_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    date_from = models.DateField()
    date_to = models.DateField()
    expected_number_of_attendees = models.IntegerField()
    expected_budget = models.IntegerField()

    approved_by_senior_customer_service_officer = models.BooleanField(default=False)
    approved_by_financial_manager = models.BooleanField(default=False)
    approved_by_admin_manager = models.BooleanField(default=False)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='event_requests_created'
    )


class SubteamTask(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class STATUS:
        todo = 'todo'
        in_progress = 'in_progress'
        done = 'done'

    STATUS_CHOICES = (
        (STATUS.todo, 'todo'),
        (STATUS.in_progress, 'in_progress'),
        (STATUS.done, 'done')
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS.todo)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='subteam_tasks'
    )


class ExtraBudgetRequest(models.Model):
    amount_required = models.IntegerField()
    reason = models.CharField(max_length=255)

    class STATUS:
        requested = 'requested'
        negotiating = 'negotiating'
        accepted = 'accepted'
        rejected = 'rejected'

    STATUS_CHOICES = (
        (STATUS.requested, 'requested'),
        (STATUS.negotiating, 'negotiating'),
        (STATUS.accepted, 'accepted'),
        (STATUS.rejected, 'rejected'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS.requested)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='extra_budget_requests'
    )


class StaffRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class CONTRACT_TYPE:
        full_time = 'full_time'
        part_time = 'part_time'


    CONTRACT_TYPE_CHOICES = (
        (CONTRACT_TYPE.full_time, 'full_time'),
        (CONTRACT_TYPE.part_time, 'part_time')
    )
    contract_type = models.CharField(max_length=50, choices=CONTRACT_TYPE_CHOICES, default=CONTRACT_TYPE.full_time)
    years_of_experience = models.IntegerField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='staff_requests'
    )

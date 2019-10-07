from django.db import models


class EventRequestApplication(models.Model):
    event_name = models.CharField(max_length=255, default='')
    client_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    date_from = models.DateField()
    date_to = models.DateField()
    expected_number_of_attendees = models.IntegerField()
    expected_budget = models.IntegerField()

    class STATUS:
        created = 'created'
        approved_by_scs = 'approved_by_scs'

    STATUS_CHOICES = (
        (STATUS.created, 'created'),
        (STATUS.approved_by_scs, 'approved_by_scs')
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS.created)

    approved_by_senior_customer_service_officer = models.BooleanField(default=False)
    approved_by_financial_manager = models.BooleanField(default=False)
    approved_by_admin_manager = models.BooleanField(default=False)


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

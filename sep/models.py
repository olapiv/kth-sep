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

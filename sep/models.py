from django.db import models


# Create your models here.


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




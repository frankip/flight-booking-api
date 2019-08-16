from django.db import models

# Create your models here.


class Tickets(models.Model):
    ticket_holder = models.CharField(max_length=200, blank=True, default='')
    ticket_number = models.CharField(max_length=200, blank=True, default='')
    flight_number = models.CharField(max_length=200, blank=True, default='')
    destination = models.CharField(max_length=200, blank=True, default='')
    status = models.BooleanField(default=False)
    flight_time = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('ticket_number',)
    

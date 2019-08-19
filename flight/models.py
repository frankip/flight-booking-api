from django.db import models

# Create your models here.


class FlightTickets(models.Model):
    RESERVED = 'Reserved'
    AVAILABLE = 'Available'
    TICKET_STATUS = [
         (RESERVED, 'Reserved'),
         (AVAILABLE, 'Available'),
    ]
    passenger = models.CharField(max_length=200, blank=True, verbose_name='Name Of Pasenger')
    origin = models.CharField(max_length=200, blank=True, verbose_name='From')
    flight_number = models.IntegerField(blank=True, default='')
    destination = models.CharField(max_length=200, blank=True, default='')
    status = models.CharField(
        max_length=10,
        choices=TICKET_STATUS,
        default=AVAILABLE,
    )
    time = models.DateTimeField(verbose_name='Date of depature')
    seat_number = models.IntegerField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.passenger
    

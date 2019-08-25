from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

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


class UserProfile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=17, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    images = models.CharField(max_length=17, blank=True, verbose_name='passport image')

    @receiver(post_save, sender=get_user_model())
    def create_user_profile(sender, instance=None, created=False, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    def __str__(self):
        return self.user


class PassportImage(models.Model):
    image_url = models.CharField(max_length=30, blank=True)
        # user = models.ForeignKey(User, on_delete=models.CASCADE)
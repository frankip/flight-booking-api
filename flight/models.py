from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from cloudinary.models import CloudinaryField

# Create your models here.


class Flight(models.Model):
    BOOKED = 'Booked'
    AVAILABLE = 'Available'
    TICKET_STATUS = [
         (BOOKED, 'Booked'),
         (AVAILABLE, 'Available'),
    ]
    name = models.CharField(max_length=200, blank=True, verbose_name='Name Of flight')
    origin = models.CharField(max_length=200, blank=True, verbose_name='From')
    destination = models.CharField(max_length=200, blank=True, default='')
    status = models.CharField(
        max_length=10,
        choices=TICKET_STATUS,
        default=AVAILABLE,
    )
    date = models.DateField(verbose_name='Date of depature')
    time = models.TimeField(verbose_name='Time of depature')
    # bookings = models.ForeignKey('FlightBooking', related_name='booking', on_delete=models.CASCADE, blank=True,)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


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


class Image(models.Model):
    # image_url = models.CharField(max_length=30, blank=True)
    image = CloudinaryField('image')

        # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.image


class FlightBooking(models.Model):
    booking_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField(default=1)
    ticket_type = models.CharField(max_length=30, default='economy')

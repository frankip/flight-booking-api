from rest_framework import serializers
from flight.models import (
    Flight, 
    UserProfile,
    FlightBooking
    )

from rest_auth.serializers import UserDetailsSerializer


class FlightSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Flight
        # fields = [
        #     'url',
        #     'id',
        #     'passenger',
        #     'origin',
        #     'destination',
        #     'flight_number',
        #     'time',
        #     'seat_number',
        #     'status'
        # ]
        fields = '__all__'
        # exclude = ('bookings',)


class UserProfileSerializer(UserDetailsSerializer):
    user = UserDetailsSerializer()

    class Meta:
        model = UserProfile
        # fields = ['user', 'phone_number', 'bio', 'location', 'birth_date']
        fields = '__all__'
        # exclude = ('user', )


class FlightBookingSerializer(serializers.HyperlinkedModelSerializer):
    flight = serializers.PrimaryKeyRelatedField(queryset=Flight.objects.all())
    class Meta:
        model = FlightBooking
        fields = ['url','flight', 'number_of_tickets', 'ticket_type']
        read_only_fields = ('flight',)

class FlightBookingDetailSerializer(FlightBookingSerializer):

    flight = FlightSerializer(read_only=True)
from rest_framework import serializers
from flight.models import FlightTickets, UserProfile

from rest_auth.serializers import UserDetailsSerializer


class FlightTicketSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FlightTickets
        fields = [
            'url',
            'id',
            'passenger',
            'origin',
            'destination',
            'flight_number',
            'time',
            'seat_number',
            'status'
        ]


class UserProfileSerializer(UserDetailsSerializer):
    user = UserDetailsSerializer()


    class Meta:
        model = UserProfile
        # fields = ['user', 'phone_number', 'bio', 'location', 'birth_date']
        fields = '__all__'
        # exclude = ('user', )

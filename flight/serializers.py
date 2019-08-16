from rest_framework import serializers
from flight.models import Tickets


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = (
            'id',
            'ticket_number',
            'flight_number',
            'destination',
            'flight_time',
            'ticket_holder',
            'status'
        )
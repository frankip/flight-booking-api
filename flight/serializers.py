from rest_framework import serializers
from flight.models import FlightTickets


class FlightTicketSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='FlightTicketList',
    # )

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

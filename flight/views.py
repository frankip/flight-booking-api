from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.response import Response

from flight.serializers import FlightTicketSerializer
from flight.models import FlightTickets


# Create your views here.
class FlightTicketList(generics.ListCreateAPIView):
    queryset = FlightTickets.objects.all()
    serializer_class = FlightTicketSerializer
    name = 'flighttickets-list'


class FlightTicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlightTickets.objects.all()
    serializer_class = FlightTicketSerializer
    name = 'flighttickets-detail'


class ApiRoot(generics.GenericAPIView): 
    name = 'api-root' 
    def get(self, request): 
        return Response({ 
            'tickets': reverse(FlightTicketList.name, request=request),
            }) 
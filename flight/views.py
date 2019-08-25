from rest_framework.reverse import reverse
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.views.generic import View

from rest_auth import views

from flight.serializers import FlightTicketSerializer, UserProfileSerializer
from flight.models import FlightTickets, UserProfile


# Create your views here.
class FlightTicketList(generics.ListCreateAPIView):
    queryset = FlightTickets.objects.all()
    serializer_class = FlightTicketSerializer
    permission_classes = [IsAuthenticated]
    name = 'flighttickets-list'


class FlightTicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlightTickets.objects.all()
    serializer_class = FlightTicketSerializer
    name = 'flighttickets-detail'


class UserProfileView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    name = 'userprofile'

    def get_queryset(self):
        # print('--->>>>',)
        return self.queryset.filter(user=self.request.user)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request):
        return Response({
            'tickets': reverse(FlightTicketList.name, request=request),
            'login': reverse('rest_login', request=request),
            'logout': reverse("rest_logout", request=request),
            'profile': reverse(UserProfileView.name, request=request),
            })
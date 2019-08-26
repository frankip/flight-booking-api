from rest_framework.reverse import reverse
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import permissions

from django.views.generic import View

from rest_auth import views

from flight.serializers import (
    FlightSerializer, 
    UserProfileSerializer,
    FlightBookingSerializer,
    FlightBookingDetailSerializer,
    )
from flight.models import (
    Flight,
    UserProfile,
    FlightBooking
    )


# Create your views here.
class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = 'flight-list'


class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    name = 'flight-detail'


class UserProfileView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = 'userprofile'

    def get_queryset(self):
        # print('--->>>>',)
        return self.queryset.filter(user=self.request.user)


class FlightBookingList(generics.ListCreateAPIView):
    queryset = FlightBooking.objects.all()
    serializer_class = FlightBookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = 'flightbooking-list'

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer): # new
        serializer.save(user=self.request.user)


class FlightBookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlightBooking.objects.all()
    serializer_class = FlightBookingDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    name = 'flightbooking-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request):
        return Response({
            'flights': reverse(FlightList.name, request=request),
            'login': reverse('rest_login', request=request),
            'logout': reverse("rest_logout", request=request),
            'profile': reverse(UserProfileView.name, request=request),
            'booking': reverse(FlightBookingList.name, request=request),
            })
from rest_framework import serializers
from cloudinary.templatetags import cloudinary

from flight.models import (
    Flight, 
    UserProfile,
    FlightBooking,
    Image
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
    user = UserDetailsSerializer(read_only=True)

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

class FileUploadSerializer(serializers.Serializer):
    # I set use_url to False so I don't need to pass file 
    # through the url itself - defaults to True if you need it
    image = serializers.FileField(use_url=False)

    class Meta:
        model = Image
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(FileUploadSerializer, self).to_representation(instance)
        imageUrl = cloudinary.utils.cloudinary_url(
            instance.image, width=100, height=150, crop='fill')

        representation['image'] = imageUrl[0]
        return representation
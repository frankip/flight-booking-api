from random import randint
from rest_framework.reverse import reverse
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import permissions, parsers
from django.views.generic import View
from rest_framework import status

from rest_auth import views
from cloudinary.templatetags import cloudinary

from flight.serializers import (
    FlightSerializer, 
    UserProfileSerializer,
    FlightBookingSerializer,
    FlightBookingDetailSerializer,
    FileUploadSerializer
    )
from flight.models import (
    Flight,
    UserProfile,
    FlightBooking,
    Image
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


# views.py
class FileUploadView(views.APIView):
    # parser_classes = [parsers.FileUploadParser]
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)
    serializer_class = FileUploadSerializer
    name = 'file-upload'

    def get(self, request, format=None):
        images = Image.objects.all()
        serializer = FileUploadSerializer(images, many=True)
        return Response({'images': serializer.data}, status=status.HTTP_200_OK)

    def upload_image_cloudinary(self, request, image_name):
        print('popin---->>>>', request.FILES['image'])
        cloudinary.uploader.upload(
            cloudinary.config( 
                cloud_name = "francky", 
                api_key = "XfqzOSKfgU3cNz2OafXz6o4-M8o", 
                api_secret = "XfqzOSKfgU3cNz2OafXz6o4-M8o1" 
                ),
            request.FILES['image'],
            public_id=image_name,
            tags=['image_ad', 'NAPI']
        )
        print('popin---->>>>2', image_name)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                imageName = 'passport_v{0}'.format(randint(0, 100))
                self.upload_image_cloudinary(request, imageName)
                serializer.save(image_ad=imageName)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                return Response({'image': 'Please upload a valid image'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(serializer)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, filename, format=None):
    #     serializer = FileUploadSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     file_obj = request.data['file']

    #     print('----------->>', file_obj)

    #     # ...
    #     # do some stuff with uploaded file
    #     # ...
    #     return Response(status=204)


    # def put(self, request, filename, format=None):
    #     serializer = FileUploadSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     file_obj = request.data['file']

    #     print('----------->>', file_obj)

    #     # ...
    #     # do some stuff with uploaded file
        # ...
        return Response(status=204)


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
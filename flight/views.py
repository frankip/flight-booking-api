from random import randint
import pprint
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions, parsers
from rest_framework import status

from rest_auth import views
from cloudinary.templatetags import cloudinary
import cloudinary.uploader
# from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

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
        serializer = FileUploadSerializer()
        return Response({'images': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        images = Image.objects.all()
        serializer = FileUploadSerializer(data=request.FILES)
        file_name = request.FILES.get('image')
        imageName = 'passport_v{0}'.format(randint(0, 100))
        resp = cloudinary.uploader.upload(file_name, public_id=imageName)

        url, options = cloudinary_url(
            resp['public_id'],
            format=resp['format'],
            width=200,
            height=150,
            crop="scale",
        )

        # print("url------->1 " + url)

        # serializer = FileUploadSerializer(data=request.FILES)
        
        print("url------->0 ",serializer.is_valid())
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        if serializer.is_valid():
            
            images.save(image=url)
            pprint.pprint(serializer.image)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("url------->2 ", url)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, format=None):
    #     serializer = FileUploadSerializer(data=request.FILES)
    #     print('>>>>>>>>>', serializer)
    #     if serializer.is_valid():
    #         file_name = request.FILES['image']
    #         imageName = 'passport_v{0}'.format(randint(0, 100))
    #         response = cloudinary.uploader.upload(file_name)

    #         url, options = cloudinary_url(
    #             response['public_id'],
    #             format=response['format'],
    #             width=200,
    #             height=150,
    #             crop="scale",
    #         )

    #         # print("scaling to 200x150 url: " + url)
    #         serializer.save(image=url, options=options)
    #         # def create(self, validated_data):
    #         #     return Image.objects.create(**response)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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



# Everything working okay isipokuwa the uploading image, tumefuata tukafika apo kwa call back za cloudinary tukakwamia apao
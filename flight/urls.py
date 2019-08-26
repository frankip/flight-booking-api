from django.urls import path
from flight import views

urlpatterns = [
    path('', views.ApiRoot.as_view(),
    name=views.ApiRoot.name),

    path('flights', views.FlightList.as_view(),
    name=views.FlightList.name),
    path('flights/<int:pk>/', views.FlightDetail.as_view(),
    name=views.FlightDetail.name),

    path('profile', views.UserProfileView.as_view(),
    name=views.UserProfileView.name),
    path('profile/<int:pk>/', views.UserProfileView.as_view(),
    name=views.UserProfileView.name),

    path('booking', views.FlightBookingList.as_view(),
    name=views.FlightBookingList.name),
    path('booking/<int:pk>/', views.FlightBookingDetail.as_view(),
    name=views.FlightBookingDetail.name),

    path('upload/', views.FileUploadView.as_view(),
    name=views.FileUploadView.name),

]
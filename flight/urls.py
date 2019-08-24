from django.urls import path
from flight import views

urlpatterns = [
    path('', views.ApiRoot.as_view(),
    name=views.ApiRoot.name),

    path('tickets', views.FlightTicketList.as_view(),
    name=views.FlightTicketList.name),
    path('tickets/<int:pk>/', views.FlightTicketDetail.as_view(),
    name=views.FlightTicketDetail.name)
]
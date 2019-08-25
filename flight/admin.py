from django.contrib import admin
from flight.models import FlightTickets, UserProfile


class FlightAdmin(admin.ModelAdmin):
    list_display = [f.name for f in FlightTickets._meta.get_fields()]
    search_fields = ('passenger', 'status', 'destination', 'time',)
    list_editable = ('destination', 'origin')
    list_filter = ('status', 'time',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in UserProfile._meta.get_fields()]


admin.site.register(FlightTickets, FlightAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
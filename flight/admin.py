from django.contrib import admin
from flight.models import FlightTickets


class FlightAdmin(admin.ModelAdmin):
    list_display = [f.name for f in FlightTickets._meta.get_fields()]
    search_fields = ('passenger', 'status', 'destination', 'time',)
    list_editable = ('destination', 'origin')
    list_filter = ('status', 'time',)
    
    # fields = ['type', ]


admin.site.register(FlightTickets, FlightAdmin)
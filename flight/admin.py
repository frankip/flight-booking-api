from django.contrib import admin
from flight.models import Flight, UserProfile, FlightBooking


class FlightAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Flight._meta.fields]
    search_fields = ('name', 'status', 'destination', 'date',)
    list_editable = ('destination', 'origin')
    list_filter = ('status', 'date',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in UserProfile._meta.get_fields()]


admin.site.register(Flight, FlightAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FlightBooking) 
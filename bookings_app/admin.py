from django.contrib import admin

# Register your models here.

from .models import Participant, Booking

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'participant', 'booking_date', 'confirmed')
    list_filter = ('confirmed', 'booking_date')
    search_fields = ('event__title', 'participant__first_name', 'participant__last_name')

admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Booking, BookingAdmin)
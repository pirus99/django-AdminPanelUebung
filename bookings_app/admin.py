from django.contrib import admin

# Register your models here.

from .models import Participant, Booking

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

    def save_model(self, request, obj, form, change):
        obj.fullname = f"{obj.first_name} {obj.last_name}"
        super().save_model(request, obj, form, change)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'participant', 'booking_date', 'confirmed')
    list_filter = ('confirmed', 'booking_date')
    search_fields = ('event__title', 'participant__first_name', 'participant__last_name')
    readonly_fields = ('booking_date',)

admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Booking, BookingAdmin)
from django.contrib import admin

# Register your models here.

from .models import EventCategory, Location, Event

admin.site.register(EventCategory)
admin.site.register(Location)
admin.site.register(Event)

from django.contrib import admin

# Register your models here.

from .models import EventCategory, Location, Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'date')
    list_filter = ('category', 'location', 'date')
    search_fields = ('title',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(EventCategory, EventCategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
    
from django.contrib import admin

from .models import EventCategory, Location, Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'date')
    list_filter = ('category', 'location', 'date')
    search_fields = ('title',)

    fieldsets = (
        ('Allgemein', {
            'fields': ('title', 'category', 'date'),
        }),
        ('Organisation', {
            'classes': ('collapse',),
            'fields': ('location', 'capacity'),
        }),
    )

    date_hierarchy = 'date'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        for fname in ('location', 'capacity'):
            if fname in form.base_fields:
                form.base_fields[fname].required = False
        return form

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(EventCategory, EventCategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
    
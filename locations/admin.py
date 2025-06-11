from django.contrib import admin
from .models import Location, LocationImage

class LocationImageInline(admin.TabularInline):
    model = LocationImage
    extra = 1

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'price')
    inlines = [LocationImageInline]

admin.site.register(LocationImage)

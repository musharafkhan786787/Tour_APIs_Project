from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'booking_date', 'price', 'status', 'created_at')
    list_filter = ('booking_date', 'status')
    search_fields = ('user__email', 'location__name')

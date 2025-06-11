from django.db import models
from django.conf import settings
from locations.models import Location  # Import Location from locations app

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    booking_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # ✅ Added
    status = models.CharField(max_length=20, default='confirmed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} booked {self.location.name} on {self.booking_date}"

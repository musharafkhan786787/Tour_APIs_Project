from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

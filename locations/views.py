from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Location
from .serializers import LocationSerializer

class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

class LocationByNameView(generics.RetrieveAPIView):
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        name = self.kwargs['name']
        return get_object_or_404(Location, name=name)

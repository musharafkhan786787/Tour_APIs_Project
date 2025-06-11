from rest_framework import serializers
from .models import Location, LocationImage

class LocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationImage
        fields = ['image_url']

class LocationSerializer(serializers.ModelSerializer):
    images = LocationImageSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ['name', 'description', 'url', 'price', 'images']

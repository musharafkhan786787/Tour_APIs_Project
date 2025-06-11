from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class LocationImage(models.Model):
    location = models.ForeignKey(Location, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self):
        return f"Image for {self.location.name}"

from django.urls import path
from .views import LocationListView, LocationByNameView

urlpatterns = [
    path('', LocationListView.as_view(), name='location-list'),
    path('name/<str:name>/', LocationByNameView.as_view(), name='location-by-name'),
]

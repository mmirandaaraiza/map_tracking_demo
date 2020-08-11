from django.urls import path, include

from rest_framework import routers

from root.vehicles.api import viewsets as vehicle_viewsets

router = routers.DefaultRouter()
router.register('vehicles', vehicle_viewsets.VehicleViewSet, 'vehicle')

urlpatterns = [
    path('', include(router.urls))
]

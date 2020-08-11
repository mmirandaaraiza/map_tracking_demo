from rest_framework import viewsets, permissions

from . import serializers
from ..models import Vehicle
from root.api.permissions import IsOwner


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VehicleSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [IsOwner]
        return super().get_permissions()

    def get_queryset(self):
        if self.action == 'list':
            return Vehicle.objects.filter(owner=self.request.user)
        return Vehicle.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

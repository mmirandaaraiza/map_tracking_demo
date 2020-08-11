from rest_framework import serializers

from ..models import Vehicle


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle

        fields = ['id', 'plate', 'lat', 'long', 'url']

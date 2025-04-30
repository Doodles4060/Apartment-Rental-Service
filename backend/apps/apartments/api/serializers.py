from rest_framework import serializers

from .models import Apartment

class ApartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'price',
            'number_of_rooms',
            'square',
            'availability',
            'owner',
            'created_at',
            'updated_at'
        ]



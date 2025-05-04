from rest_framework import serializers

from apps.apartments.models import Apartment
# from apps.users.api.serializers import UserSerializer

class ApartmentsSerializer(serializers.ModelSerializer):

    # for nested serialization
    # owner = UserSerializer(read_only=True)

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
    read_only_fields = ['id', 'created_at', 'updated_at']

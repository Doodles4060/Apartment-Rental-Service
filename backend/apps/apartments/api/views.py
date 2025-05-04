from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import views
from rest_framework import generics
from django.db.models import Q

from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
)

from .serializers import ApartmentsSerializer
from .paginations import ApartmentPagination
from .permissions import IsOwner
from apps.apartments.models import Apartment

def str_to_bool(value: str) -> bool:
    """
    Convert a string representation of a boolean to a boolean value.
    """
    if value.lower() in ["true", "1", "yes"]:
        return True
    if value.lower() in ["false", "0", "no"]:
        return False
    raise ValueError("Invalid boolean value: {}".format(value))

class ApartmentListViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentsSerializer
    lookup_field = 'slug'

    permission_classes = [permissions.AllowAny]
    # search_fields = ['name', 'description']
    pagination_class = ApartmentPagination

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = []
        match self.action:
            case 'list':
                permission_classes = [permissions.AllowAny]
            case 'create':
                permission_classes = [permissions.IsAuthenticated]
            case 'retrieve':
                permission_classes = [permissions.AllowAny]
            case 'update':
                permission_classes = [IsOwner]
            case 'partial_update':
                permission_classes = [IsOwner]
            case 'destroy':
                permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Apartment.objects.all()

        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')
        rooms = self.request.query_params.get('rooms')
        available = self.request.query_params.get('available')
        search = self.request.query_params.get('search')

        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        if rooms:
            queryset = queryset.filter(number_of_rooms=rooms)
        if available:
            try:
                available = str_to_bool(available)
                queryset = queryset.filter(availability=available)
            except ValueError:
                queryset = queryset.none()  # Invalid boolean value, return empty queryset
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )

        return queryset

    # swagger documentation with drf-spectacular
    @extend_schema(
        description='Apartment list with filters',
        parameters=[
            OpenApiParameter(
                name='price_min',
                description='Filter by minimum price',
                required=False,
                type=float
            ),
            OpenApiParameter(
                name='price_max',
                description='Filter by maximum price',
                required=False,
                type=float
            ),
            OpenApiParameter(
                name='rooms',
                description='Filter by number of rooms',
                required=False,
                type=int
            ),
            OpenApiParameter(
                name='available',
                description='Filter by availability (true/false)',
                required=False,
                type=bool
            ),
            OpenApiParameter(
                name='search',
                description='Search by name or description',
                required=False,
                type=str
            ),
        ],
        examples=[
            OpenApiExample(
                'Example of a successful request',
                value={
                    "id": 1,
                    "name": "Apartment 1",
                    "slug": "apartment-1",
                    "description": "Description of Apartment 1",
                    "price": 100000.0,
                    "number_of_rooms": 3,
                    "square": 75.0,
                    "availability": True,
                    "owner": 1,
                    "created_at": "2023-01-01T00:00:00Z",
                    "updated_at": "2023-01-01T00:00:00Z"
                },
                response_only=True
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description='',
        
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
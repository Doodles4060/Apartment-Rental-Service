from rest_framework.pagination import PageNumberPagination

class ApartmentPagination(PageNumberPagination):
    """Pagination class for apartment list view."""
    page_size = 10
from django.contrib import admin

from .models import Apartment

@admin.register(Apartment)
class CustomApartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'number_of_rooms', 'square', 'availability', 'owner', 'created_at', 'updated_at']
    list_filter = ['availability']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug', 'description']

    fieldsets = (
        (None, {'fields': ('slug',)}),
        ('General', {'fields': ('name', 'description', 'price')}),
        ('Measurements', {'fields': ('number_of_rooms', 'square')}),
        ('Availability', {'fields': ('availability', 'owner',)}),
    )

    filter_horizontal = ()
    ordering = ('-created_at',)

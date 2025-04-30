from django.contrib import admin

from .models import Apartment

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'number_of_rooms', 'square', 'availability', 'owner', 'created_at', 'updated_at')
    list_filter = ['availability']
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)

admin.site.register(Apartment, ApartmentAdmin)

from django.db import models

class Apartment(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,
                            help_text="You can set it manually. "
                                      "However, if you choose to type in name first it will affect the slug field.")
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text='8 digits max, 2 decimal places')
    number_of_rooms = models.IntegerField()
    square = models.DecimalField(max_digits=8, decimal_places=2, help_text='8 digits max, 2 decimal places')
    availability = models.BooleanField(default=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
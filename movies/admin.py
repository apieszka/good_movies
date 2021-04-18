from django.contrib import admin

# Register your models here.
from movies.models import Movie, Director, Review # NOWE


admin.site.register(Movie) # NOWE
admin.site.register(Director)
admin.site.register(Review)

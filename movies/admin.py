from django.contrib import admin
from movies.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    autocomplete_fields = ['actors']
    list_display = ("id", "title", "genre", "release_dat", "resume")

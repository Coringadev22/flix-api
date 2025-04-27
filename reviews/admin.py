from django.contrib import admin
from reviews.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "get_movie_title", "stars", "comment")

    def get_movie_title(self, obj):
        return obj.movie.title
    get_movie_title.short_description = 'Movie'
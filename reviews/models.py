from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie 

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name="reviews")
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "Avaliacao de 1 a 5"),
            MaxValueValidator(5, "Avaliacao de 1 a 5" ),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Review for {self.movie}"


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)  # Movie title (string, max 200 chars)
    tmdb_id = models.CharField(max_length=50, unique=True)  # Unique TMDB movie ID (string, max 50 chars)
    poster_url = models.URLField(blank=True, null=True)  # Optional URL to the movie poster

    def __str__(self):
        return self.title
    
class UserMovieList(models.Model):
    STATUS_CHOICES = [
        ("watchlist", "Watchlist"),  # User wants to watch
        ("watched", "Watched"),      # User has watched
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the user
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Reference to the movie
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)  # Status: "watchlist" or "watched"

    class Meta:
        unique_together = ("user", "movie", "status")  # Ensures unique (user, movie, status) combinations

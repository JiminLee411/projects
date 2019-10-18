from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=455)
    title_en = models.CharField(max_length=455)
    audience = models.IntegerField()
    open_data = models.DateField()
    genre = models.CharField(max_length=200)
    watch_grade = models.CharField(max_length=100)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

class Review(models.Model):
    content = models.CharField(max_length=455)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

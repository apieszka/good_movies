from django.db import models

# Create your models here.

class Movie(models.Model): #klasa modelowa Film dla bazy danych
    title = models.CharField(verbose_name = "Tytuł", max_length=100)
    short_description = models.TextField(verbose_name="opis")
    published_at = models.DateTimeField(verbose_name="data premiery")
    


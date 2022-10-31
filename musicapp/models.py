from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length = 300)
    last_name = models.CharField(max_length = 300, blank=True)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name  + '' +  self.last_name


class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, null=True , on_delete = models.CASCADE)
    title = models.CharField(max_length= 300)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_bio = models.CharField(max_length = 400, null=True)

    def __str__(self):
        return self.title 

class Lyrics(models.Model):
    Song = models.ForeignKey(Song, null = True , on_delete = models.CASCADE)
    content = models.CharField(max_length = 900)
    track_id = models.CharField(max_length = 300)

    def __str__(self):
        return str(self.track_id) 

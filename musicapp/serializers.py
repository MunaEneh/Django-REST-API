from rest_framework import serializers
from .models import Artiste,Song,Lyrics

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Artiste
        fields= ['id', 'first_name', 'last_name', 'age']

class SongSerializer(serializers.ModelSerializer):
    class Meta:         
        model=Song
        fields= ['id', 'title', 'date_released', 'likes', 'artiste_bio']
        
class LyricsSerializer(serializers.ModelSerializer):
    class Meta:         
        model=Lyrics
        fields= ['id', 'content', 'track_id']
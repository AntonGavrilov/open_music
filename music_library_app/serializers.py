from django.contrib.auth.models import User
from rest_framework import serializers
from  music_library_app import models


class AlbumsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Album
        fields = ('name', 'country', 'City', 'Bio')

class SongsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Album
        fields = ('name', 'country', 'City', 'Bio')

# I will be do this work later
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Photo, Author, Source
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'name', 'url')

class PhotoSerializer(GeoFeatureModelSerializer):
    """
    Serializer pour le modèle Photo au format GeoJSON.
    """
    author_name = serializers.SerializerMethodField()
    source_name = serializers.SerializerMethodField()
    source_url = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        return obj.author.name if obj.author else None

    def get_source_name(self, obj):
        return obj.source.name if obj.source else None

    def get_source_url(self, obj):
        return obj.source.url if obj.source else None

    class Meta:
        model = Photo
        geo_field = 'location'
        fields = ('id', 'title', 'image', 'image_url', 'description', 'year', 'is_approximate', 
                  'author_name', 'source_name', 'source_url', 'azimuth')

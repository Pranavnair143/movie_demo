from django.contrib.auth import get_user_model
from rest_framework import serializers

from movie.models import Collection

User = get_user_model()

class CollectionCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Collection
        fields = ['title', 'description', 'movies', 'user']

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)


class CollectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['title', 'description', 'movies']

    def validate(self, attrs):
        if self.obj.user.pk != self.context('request').user.pk:
            raise serializers.ValidationError("You are not authenticated to edit this collection")
        return attrs


class CollectionReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ['uuid', 'title', 'description', 'movies']


class CollectionListObjSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ['uuid', 'title', 'description']


class CollectionListSerializer(serializers.Serializer):
    collections=CollectionListObjSerializer(many=True)
    favourite_genres= serializers.SerializerMethodField()

    def get_favourite_genres(self, obj):
        collections = obj.get("collections")
        genre_map = {}
        for collection in collections:
            for movie in  collection.movies:
                if genres := movie.get("genres"):
                    for genre in genres.split(','):
                        if genre not in genre_map.keys():
                            genre_map[genre] = 1
                        else:
                            genre_map[genre] += 1
        return [genre for genre, count in sorted(genre_map.items(), key=lambda x: x[1], reverse=True)[:3]]
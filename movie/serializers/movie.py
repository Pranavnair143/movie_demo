from rest_framework import serializers

class MovieReadSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    genres = serializers.CharField(required=False)
    uuid = serializers.UUIDField()
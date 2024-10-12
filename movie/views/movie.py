import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from movie.serializers import MovieReadSerializer
from core import config, constants

class MovieViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        page = request.query_params.get('page', "1")

        response = requests.get(
            config.MOVIES_API_URL.format(page=page),
            auth=(config.MOVIES_API_AUTH_USERNAME, config.MOVIES_API_AUTH_PASSWORD),
            verify=False
        )

        if response.status_code == 200:
            data = response.json()

            movies = data.get('results', [])
            serializer = MovieReadSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"error": constants.FETCH_MOVIES_FAILURE_MSG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

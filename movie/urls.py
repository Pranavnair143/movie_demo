from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie.views import MovieViewSet, CollectionViewSet


collection_router = DefaultRouter()
collection_router.register(r'', CollectionViewSet, basename='collection')


urlpatterns = [
    path('movies', MovieViewSet.as_view(), name='movie-list'),
    path('collection/<uuid:uuid>/', CollectionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('collection/',CollectionViewSet.as_view({'get': 'list', 'post': 'create'})),
]

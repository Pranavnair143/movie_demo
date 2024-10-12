from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from movie.models import Collection
from movie.serializers.collection import CollectionCreateSerializer, CollectionReadSerializer, CollectionListSerializer
from core import constants

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_classes = {
        "list": CollectionListSerializer,
        "retrieve": CollectionReadSerializer,
        "create": CollectionCreateSerializer,
        "update": CollectionCreateSerializer,
    }
    lookup_field = 'uuid'

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().filter(user=request.user)

        serializer = self.get_serializer_class()(instance={"collections": qs.all()})
        return Response({'status': False, "data": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer_class()(obj, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer_class()(data=data, context={"request": request})
        if serializer.is_valid():
            obj = serializer.save()
            return Response({'collection_uuid': str(obj.uuid)})

        return Response({'status': False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        serializer = self.get_serializer_class()(instance=instance, data=data, context={'request': request})
        if serializer.is_valid():
            obj = serializer.update(instance, serializer.validated_data)
            return Response({'collection_uuid': str(obj.uuid)})

        return Response({'status': False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response({'status': True, "detail": constants.COLLECTION_DELETE_SUCCESS_MSG}, status=status.HTTP_200_OK)
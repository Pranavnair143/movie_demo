from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from user.models import AppSettings
from core import constants

class AppSettingsViewSet(viewsets.ModelViewSet):
    queryset = AppSettings.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def list(self, request, *args, **kwargs):
        settings = self.get_queryset().first()
        return Response({"request_count":settings.request_count}, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def reset(self, request):
        settings = self.get_queryset().first()
        settings.request_count = 0
        settings.save()
        return Response({"message": constants.REQUEST_COUNT_SUCCESS_MSG}, status=status.HTTP_200_OK)


from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin

from user.models import AppSettings

class RequestMiddleware(MiddlewareMixin):
    """
    Middleware to count request count
    """
    def process_request(self, request):
        settings = AppSettings.objects.all().first()
        settings.request_count += 1
        settings.save()

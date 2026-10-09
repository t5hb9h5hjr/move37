from django.http import HttpResponse

from .constants import DEFAULT_GREETING
from .models import Greeting


def index(request):
    message = (
        Greeting.objects.filter(active=True)
        .order_by("-pk")
        .values_list("message", flat=True)
        .first()
    )
    return HttpResponse(
        message if message is not None else DEFAULT_GREETING,
        content_type="text/plain; charset=utf-8",
    )

from django.http import HttpResponse

from .constants import DEFAULT_GREETING
from .models import Greeting


def index(request):
    greeting = Greeting.objects.filter(active=True).order_by("-pk").first()
    return HttpResponse(
        greeting.message if greeting else DEFAULT_GREETING,
        content_type="text/plain; charset=utf-8",
    )

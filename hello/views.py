from django.http import HttpResponse

from .models import Greeting


def index(request):
    greeting = Greeting.objects.filter(active=True).last()
    return HttpResponse(greeting.message if greeting else "hello claude, I am gpt")

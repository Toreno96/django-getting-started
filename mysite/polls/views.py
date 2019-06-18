import logging

from django.http import HttpResponse


def index(request, **kwargs):
    logging.getLogger('django.server').info(kwargs)
    return HttpResponse("Hello, world. You're at the polls index.")

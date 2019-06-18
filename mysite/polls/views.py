import logging

from django.http import HttpResponse

from polls.models import Question


def index(request, **kwargs):
    logging.getLogger('django.server').info(kwargs)
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    latest_questions = ', '.join([q.question_text for q in latest_questions])
    return HttpResponse(latest_questions)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

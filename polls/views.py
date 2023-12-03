from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_questions": latest_questions}
    return render(request, "polls/index.html", context=context)


def vote(request, question_id):
    return HttpResponse(f"Votes gained for this {question_id} are")


def detail(request, question_id):
    return HttpResponse(f"Detail about this {question_id} is")


def results(request, question_id):
    return HttpResponse(f"Results for {question_id} are")

from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Question,Choice
from django.template import loader

# Create your views here.

def index(request):
    list_q = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'list_q':list_q,
    }
    return render(request, 'polls/index.html',context=context)

def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist :
        raise Http404("Question does not exist")
    return render(request,'polls/details.html',context={'question':question})

def results(request, question_id):
    response = "results for this question are:\n"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)


from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    all_questions = Question.objects.all()
    all_questions_time = all_questions.order_by('-time')
    template = loader.get_template('home/home.html')
    context = {
        'all_questions': all_questions,
        'all_questions_time': all_questions_time,
    }
    return HttpResponse(template.render(context, request))

def question(request, question_id):
    return HttpResponse("<h2>Question " + str(question_id) + "</h2>")
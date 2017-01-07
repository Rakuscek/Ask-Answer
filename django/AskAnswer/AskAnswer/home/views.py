from django.http import Http404
from django.shortcuts import render

from .models import Question, Answer

def index(request):
    all_questions = Question.objects.all()
    all_questions_time = all_questions.order_by('-time')
    context = {
        'all_questions': all_questions,
        'all_questions_time': all_questions_time,
    }
    return render(request, 'home/home.html', context)

def question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question not found")

    all_questions_time = Question.objects.all().order_by('-time')
    all_answers = question.answer_set.all()
    context = {
        'question': question,
        'all_answers': all_answers,
        'all_questions_time': all_questions_time
    }
    return render(request, 'question/question.html', context)
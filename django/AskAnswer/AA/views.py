from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
import datetime

from .models import Question, Answer

def index(request):
    all_questions = Question.objects.all()
    all_questions_time = all_questions.order_by('-time')
    context = {
        'all_questions': all_questions,
        'all_questions_time': all_questions_time,
    }
    return render(request, 'home.html', context)

def question(request, question_id):
    cer_question = get_object_or_404(Question, pk=question_id)

    all_questions_time = Question.objects.all().order_by('-time')
    all_answers = cer_question.answer_set.all()
    context = {
        'question': cer_question,
        'all_answers': all_answers,
        'all_questions_time': all_questions_time
    }
    return render(request, 'question.html', context)

def about(request):
    all_questions_time = Question.objects.all().order_by('-time')
    context = {
        'all_questions_time': all_questions_time,
    }
    return render(request, 'about.html', context)

def category(request):
    all_questions_time = Question.objects.all().order_by('-time')
    context = {
        'all_questions_time': all_questions_time,
    }
    return render(request, 'categories.html', context)

def ask(request):
    all_questions_time = Question.objects.all().order_by('-time')
    context = {
        'all_questions_time': all_questions_time,
    }
    return render(request, 'ask.html', context)
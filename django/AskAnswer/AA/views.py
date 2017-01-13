from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import *
from django.contrib.auth import authenticate, login, logout
import datetime

from .models import Question, Answer


def index(request):
    all_questions = Question.objects.all()
    all_questions_time = all_questions.order_by('-time')[:3]
    context = {
        'all_questions': all_questions,
        'all_questions_time': all_questions_time,
    }
    return render(request, 'home.html', context)


def question(request, question_id):
    cer_question = get_object_or_404(Question, pk=question_id)

    all_questions_time = Question.objects.all().order_by('-time')[:3]
    all_answers = cer_question.answer_set.all().order_by('-plusVotes')
    context = {
        'question': cer_question,
        'all_answers': all_answers,
        'all_questions_time': all_questions_time
    }
    return render(request, 'question.html', context)


def about(request):
    all_questions_time = Question.objects.all().order_by('-time')[:3]
    context = {
        'all_questions_time': all_questions_time,
    }
    return render(request, 'about.html', context)


def category(request):
    all_questions_time = Question.objects.all().order_by('-time')[:3]
    context = {
        'all_questions_time': all_questions_time,
    }
    return render(request, 'categories.html', context)


def ask(request):
    all_questions_time = Question.objects.all().order_by('-time')[:3]
    context = {
        'all_questions_time': all_questions_time,
    }
    return render(request, 'ask.html', context)


def registeruser(request):
    if request.POST:
        username = request.POST['usernameRegister']
        email = request.POST['email']
        password1 = request.POST['passwordRegister1']
        password2 = request.POST['passwordRegister2']
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            user = authenticate(username=username, password=password1)
            login(request, user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def loginuser(request):
    if request.POST:
        username = request.POST['usernameLogin']
        password = request.POST['passwordLogin']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def askquestion(request):
    categories = ''
    at_least_one = False
    try:
        if request.POST['everyday']:
            if at_least_one:
                categories = categories + ', everyday'
            else:
                categories = categories + 'everyday'
            at_least_one = True
    except:
        pass

    try:
        if request.POST['video'] is not None:
            if at_least_one:
                categories = categories + ', video'
            else:
                categories = categories + 'video'
            at_least_one = True
    except:
        pass

    try:
        if request.POST['internet'] is not None:
            if at_least_one:
                categories = categories + ', internet'
            else:
                categories = categories + 'internet'
            at_least_one = True
    except:
        pass

    try:
        if request.POST['food'] is not None:
            if at_least_one:
                categories = categories + ', food'
            else:
                categories = categories + 'food'
            at_least_one = True
    except:
        pass

    try:
        if request.POST['fashion'] is not None:
            if at_least_one:
                categories = categories + ', fashion'
            else:
                categories = categories + 'fashion'
            at_least_one = True
    except:
        pass

    try:
        if request.POST['trend'] is not None:
            if at_least_one:
                categories = categories + ', trend'
            else:
                categories = categories + 'trend'
            at_least_one = True
    except:
        pass

    try:
        if request.POST['technology'] is not None:
            if at_least_one:
                categories = categories + ', technology'
            else:
                categories = categories + 'technology'
            at_least_one = True
    except:
        pass

    try:
        if request.POST['cars'] is not None:
            if at_least_one:
                categories = categories + ', cars'
            else:
                categories = categories + 'cars'
            at_least_one = True
    except:
        pass

    try:
        if request.POST['fun'] is not None:
            if at_least_one:
                categories = categories + ', fun'
            else:
                categories = categories + 'fun'
            at_least_one = True
    except:
        pass

    try:
        if request.POST['sport'] is not None:
            if at_least_one:
                categories = categories + ', sport'
            else:
                categories = categories + 'sport'
            at_least_one = True
    except:
        pass

    try:
        if request.POST['computer'] is not None:
            if at_least_one:
                categories = categories + ', computer'
            else:
                categories = categories + 'computer'
            at_least_one = True
    except:
        pass

    try:
        if request.POST['misc'] is not None:
            if at_least_one:
                categories = categories + ', misc'
            else:
                categories = categories + 'misc'
    except:
        pass

    if request.POST:
        question = Question(title=request.POST['questionTitle'],
                            body=request.POST['questionBody'],
                            categories=categories,
                            username=request.user)
        question.save()
        all_questions_time = Question.objects.all().order_by('-time')[:3]
        all_answers = question.answer_set.all()
        context = {
            'question': question,
            'all_answers': all_answers,
            'all_questions_time': all_questions_time
        }
        return render(request, 'question.html', context)


def answerquestion(request, question_id):
    if request.POST:
        question = Question.objects.get(pk=question_id)
        question.answered = 1
        question.save()

        answer = Answer(body=request.POST['answerBody'],
                        username=request.user,
                        questionID=question)
        answer.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def upvote(request, answer_id, question_id):
    if request.POST:
        answer = Answer.objects.get(pk=answer_id)
        answer.plusVotes += 1
        answer.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote(request, answer_id, question_id):
    if request.POST:
        answer = Answer.objects.get(pk=answer_id)
        answer.plusVotes -= 1
        answer.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
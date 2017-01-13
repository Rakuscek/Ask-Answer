from django.conf.urls import url
from . import views

urlpatterns = [
    # /AA/
    url(r'^$', views.index, name='index'),

    # /AA/question/1
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name="question"),

    # /AA/question/1/upvote/1
    url(r'^question/(?P<question_id>[0-9]+)/upvote/(?P<answer_id>[0-9]+)$', views.upvote, name="upvote"),

    # /AA/question/1/downvote/1
    url(r'^question/(?P<question_id>[0-9]+)/downvote/(?P<answer_id>[0-9]+)$', views.downvote, name="downvote"),

    # /AA/question/1/answer
    url(r'^question/(?P<question_id>[0-9]+)/answer/$', views.answerquestion, name="answerquestion"),

    # /AA/categories
    url(r'^categories/$', views.category, name="category"),

    # /AA/about
    url(r'^about/$', views.about, name="about"),

    # /AA/ask
    url(r'^ask/$', views.ask, name="ask"),

    # /AA/ask/question
    url(r'^ask/question/$', views.askquestion, name="askquestion"),

    # /AA/register
    url(r'^register/', views.registeruser, name="registeruser"),

    # /AA/login
    url(r'^login/', views.loginuser, name="loginuser"),

    # /AA/logout
    url(r'^logout/', views.logoutuser, name="logoutuser"),
]
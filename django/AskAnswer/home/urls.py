from django.conf.urls import url
from . import views

urlpatterns = [
    # /home/
    url(r'^$', views.index, name='index'),

    # /home/question/1
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name="question"),
]
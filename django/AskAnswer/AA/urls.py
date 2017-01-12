from django.conf.urls import url
from . import views

urlpatterns = [
    # /AA/
    url(r'^$', views.index, name='index'),

    # /AA/question/1
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name="question"),

    # /AA/categories
    url(r'^categories/$', views.category, name="category"),

    # /AA/about
    url(r'^about/$', views.about, name="about"),

    # /AA/ask
    url(r'^ask/$', views.ask, name="ask"),
]
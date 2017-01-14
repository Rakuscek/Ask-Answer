from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question

# test for checking if Question.is_recent works properly
# the given tests are supposed to give OK response
class QuestionTests(TestCase):
    def test_is_recent(self):
        a_recent = Question(title='test_recent', body='', categories='', time=timezone.now())
        a_old = Question(title='test_recent', body='', categories='', time=timezone.now() - datetime.timedelta(days=30))

        self.assertIs(a_recent.is_recent(), True)
        self.assertIs(a_old.is_recent(), False)
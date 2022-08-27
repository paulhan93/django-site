import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    '''Questions in the Polls.'''

    # return a nice, human-readable representation of the question
    def __str__(self):
        return self.question_text

    # return true if question was published within the last day
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    '''Choices for each question.'''

    # return a nice, human-readable representation of the choice
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

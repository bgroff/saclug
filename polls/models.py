from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.datetime_safe import datetime


@python_2_unicode_compatible
class Poll(models.Model):
    question = models.TextField()
    pub_date = models.DateTimeField('date published', default=datetime.utcnow)

    def __str__(self):
        return self.question


@python_2_unicode_compatible
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

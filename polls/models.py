from django.db import models


class Poll(models.Model):
    question = models.TextField()
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.TextField()
    votes = models.IntegerField(default=0)

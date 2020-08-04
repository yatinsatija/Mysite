from django.db import models

import datetime
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date pulblished')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes= models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class PeopleCount(models.Model):
    in_time = models.DateTimeField('in timing')
    in_count= models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.in_time, self.in_count)

    

import datetime
from django.utils import timezone
from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField(verbose_name="published Date")

    def was_recently_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(to=Question, on_delete=CASCADE)
    choice_text = models.CharField(max_length=155)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


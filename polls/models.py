from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    years = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    # Will see how this plays out
    # q = Question(question_text="What's new?", pub_date=timezone.now()) 



class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name



'''
    - This should prob be in views.py:
        - Microsoft.programmer_set - makes the oop go in reverse - Taking the name of the class(lowercased) and appending _set

        - This line will give you a reverse many-to-one description

    - So when applying:
        - Microsoft.programmer_set.all():
            - It will give you [<Programmer: Stacy>, <Programmer: Kelly>]>


'''

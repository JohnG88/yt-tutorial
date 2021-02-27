from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.
'''
- These are the views one normally uses

def index(request):
    # This line gits questions from recent to oldest
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    context = {'latest_question_list': latest_question_list,}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model's manager. It raises Http404 if the object doesn't exist.
    question = get_object_or_404(Question, pk=question_id)

    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html', {'question': question})

def vote(request, question_id):
    # Learn more about race conditions using F()
    # request.POST is a dictionary-like object that lets you access submitted data by key name
    # In this case, request.POST['choice'] returns the id of the selected choice, as a string
    # request.POST values are always strings
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    
    # Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''
# These are the generic views
# Have to also add the line from django.views import generic
# Each generic view needs to know what models it is referring to using model:

# ListView is display a list of objects
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

        # Question.objects.filter(pub_date__lte=timezone.now()) returns a queryset containing Questions whose pu_date is less than or equal to - that is , earlier than or equal to -timezone.now.

# DetailView is display a detail page for a particular type of object
# By default the DetailView generic view uses <app name>/<model name>_list.html
# template_name is used to tell ListView to use "polls/index.html" template
class DetailView(generic.DetailView):
    # Question is from models.py
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        '''
        Excludes any questions that aren't published yet.
        '''
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    # Question is from models.py
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



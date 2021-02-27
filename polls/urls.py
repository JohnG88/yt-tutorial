from django.urls import path
from . import views
# To differentiate between apps just app namespace. In this case our app is polls and also change the urls in templates to 'polls:detail'

'''
- These are the views one would use

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name="index"),

    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name="detail"),

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name="results"),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name="vote"),
]
'''

# These are the generic views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
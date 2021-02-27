from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse

# Create your tests here.
# The more tests the better
# Sometime you will have to update the tests
# Good rules-of-thumb
    # a seprate TestClass for each model or view
    # a seprate test method for each set of conditions you want to test
    # test method names that describe their function


# Need to learn more about tests

# Add the Question model name to test name
'''
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        
        # was_published_recently() returns False for questions whose pub_date is in the future.
        
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
    
        # was_published_recently() returns True for questions whose pub_date is within the last day.
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
'''

# Created create_function to take out the repetition of the process of creating questions
def create_question(question_text, days):
    '''
    Create a question with the given 'question_text' and published the given number of 'days' offset to now (negative for questions published in the past, positive for questions that have yet to be published).
    '''
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    # test_no_questions doesn't create any questions, just checks the message: "no polls are available." and verifies the latest_question_list is empty
    def test_no_questions(self):
        '''
        If no questins exist, an appropriate message is displayed
        '''

        response = self.client.get(reverse('polls:index'))

        self.assertEqual(response.status_code, 200)
        # assertContains() is a django.test.TestCase additional assertion method
        self.assertContains(response, "No polls are available.")

        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # In test_past_question, we create a question and verify that it appears in the list.
    def test_past_question(self):
        '''
        Questions with a pub_date in the past are displayed on the index page.
        '''
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'], ['<Question: Past question.>']
        )

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
        # in test_future_question, we create a question with a pub_date in the future. The database is reset for each test method, so the first question is no longer there, and so again the index shouldn't have any questions in it.
    def test_future_question(self):
            '''
            Questions with a pub_date in the future aren't displayed on the index page.
            '''
            create_question(question_text="Future question.", days=30)
            response = self.client.get(reverse('polls:index'))
            self.assertContains(response, "No polls are available.")

            self.assertQuerysetEqual(response.context['latest_question_list'], [])



class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        '''
        The detail view of a quesstion with a pub-date in the future returns a 404 not found.
        '''
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_questions(self):
        '''
        The detail view of a question with a pub_date in the past displays the question's text.
        '''
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
# Test case is used to check for saving content on to database and
#  getting data back
from django.test import TestCase
from .models import Job
from django.http import HttpRequest
# SimpleTestCase is used to check the response code, 
# what html pages is rendered and etc
from django.test import SimpleTestCase
from django.urls import reverse
from . import views


# Here we are writing test case for seeing response code, 
# content inside the html page, see if right html page is rendered
class HomePageTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    
    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Joogle</h1>')
    
    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'My webpage does not contain all these')

# Below is test case for sending data on to the database and
#  checking if got the same
class JobTests(TestCase):

    def setUp(self):
        Job.objects.create(jobid = 12324, jobtitle = "Software Engineer", jobdescription = "Need to work hard")

    def test_text_content(self):
        post = Job.objects.get(jobid = 12324)
        expected_object_name = f'{post.jobtitle}'
        self.assertEquals(expected_object_name, 'Software Engineer')
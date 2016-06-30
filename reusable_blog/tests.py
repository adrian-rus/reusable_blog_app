from django.test import TestCase
from .models import Post


class PostTest(TestCase):
    # here we define the tests that we will
    # run against our Post model

    def test_str(self):
        test_title = Post(title='My Latest Blog Post')
        self.assertEquals(str(test_title),
                          'My Latest Blog Post')

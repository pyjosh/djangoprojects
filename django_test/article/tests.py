"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from article.models import Article, get_upload_file_name
from django.utils import timezone


class ArticleTest(TestCase):
    def create_article(self, title="test article", body="lorem ipsum"):
        return Article.objects.create(title=title,
                                    body=body,
                                    pub_date=timezone.now(),
                                    likes=0)

    def test_article_creation(self):
        a = self.create_article()
        self.assertTrue(isinstance(a, Article))
        self.assertEqual(a.__unicode__(), a.title)
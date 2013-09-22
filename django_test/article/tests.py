"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from article.models import Article, get_upload_file_name
from django.utils import timezone
from time import time
from django.core.urlresolvers import reverse

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

    def test_get_upload_file_name(self):
        filename = "Cheese.txt"
        path = "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)
        created_path = get_upload_file_name(self, filename)
        self.assertEqual(path, created_path)

    def test_articles_list_view(self):
        a = self.create_article()
        # get valid url which calles this view
        url = reverse('article.views.articles')
        # self.client - built in webbrowser client
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(a.title, resp.content)

    def test_article_detail_view(self):
        a = self.create_article()
        # get valid url which calles this view
        url = reverse('article.views.article', args=[a.id])
        # self.client - built in webbrowser client
        resp = self.client.get(url)

        self.assertEqual(url, a.get_absolute_url())
        self.assertEqual(resp.status_code, 200)
        self.assertIn(a.title, resp.content)


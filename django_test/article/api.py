from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Article

class ArticleResource(ModelResource):

    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        # here define what kind of filtering is allowed through the service

        # here title can be filtere in all available ways
        filtering = {'title': ALL}

        # here you can filter JUST by usin "contains"
        # filtering = {'title': "contains"}
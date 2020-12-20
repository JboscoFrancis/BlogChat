import django_filters
from django_filters import CharFilter
from . models import Post


# this filter post by title
class PostFilter(django_filters.FilterSet):
    post_title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Post
        fields = ('')
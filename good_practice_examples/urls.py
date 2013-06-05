"""URLs for the ``good_practice_examples`` app."""
from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView
from django.http import HttpResponse

from .models import GoodPracticeExample


urlpatterns = patterns(
    '',
    url(r'$',
        ListView.as_view(
            model=GoodPracticeExample,
            template_name='good_practice_examples/examples_list.html'),
        name='good_practice_example_list'),
)

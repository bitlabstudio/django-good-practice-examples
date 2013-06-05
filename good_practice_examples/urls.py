"""URLs for the ``good_practice_examples`` app."""
from django.conf.urls.defaults import patterns, url

from .views import GoodPracticeExampleListView


urlpatterns = patterns(
    '',
    url(r'$',
        GoodPracticeExampleListView.as_view(),
        name='good_practice_example_list'),
)

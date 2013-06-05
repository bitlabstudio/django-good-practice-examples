"""Tests for the views of the ``good_practice_examples`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewTestMixin


class GoodPracticeListViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ListView for GoodPracticeExample objects."""
    longMessage = True

    def get_view_name(self):
        return 'good_practice_example_list'

    def test_view(self):
        self.is_callable()

"""Tests for the models of the ``good_practice_examples`` app."""
from mock import Mock

from django.test import TestCase

from ..models import GoodPracticeExample
from .factories import (
    CountryFactory,
    GoalFactory,
    GoodPracticeExampleFactory,
    GoodPracticeExampleTranslationFactory,
    SectorFactory,
)


class CountryTestCase(TestCase):
    """Tests for the ``Country`` model."""
    longMessage = True

    def test_model(self):
        obj = CountryFactory()
        self.assertTrue(obj.pk)


class GoalTestCase(TestCase):
    """Tests for the ``Goal`` model."""
    longMessage = True

    def test_model(self):
        obj = GoalFactory()
        self.assertTrue(obj.pk)


class GoodPracticeExampleTestCase(TestCase):
    """Tests for the ``GoodPracticeExample`` model."""
    longMessage = True

    def test_model(self):
        obj = GoodPracticeExampleFactory()
        self.assertTrue(obj.pk)

    def test_manager(self):
        """
        Tests if the SimpleTranslationPublishedManager returns the correct
        objects.

        """
        # setting up the required objects
        GoodPracticeExampleTranslationFactory(is_published=True)
        GoodPracticeExampleTranslationFactory()
        GoodPracticeExampleTranslationFactory(language='de', is_published=True)
        GoodPracticeExampleTranslationFactory(language='de')

        request = Mock(LANGUAGE_CODE='en')
        self.assertEqual(
            GoodPracticeExample.objects.published(request).count(), 1,
            msg='There should be one published english practice.')

        request = Mock(LANGUAGE_CODE='de')
        self.assertEqual(
            GoodPracticeExample.objects.published(request).count(), 1,
            msg='There should be one published german practice.')

        request = Mock(LANGUAGE_CODE=None)
        self.assertEqual(
            GoodPracticeExample.objects.published(request).count(), 0,
            msg=('There should be no published practice, without a language.'))


class SectorTestCase(TestCase):
    """Tests for the ``Sector`` model."""
    longMessage = True

    def test_model(self):
        obj = SectorFactory()
        self.assertTrue(obj.pk)

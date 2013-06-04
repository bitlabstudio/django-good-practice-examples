"""Tests for the models of the ``good_practice_examples`` app."""
from django.test import TestCase

from .factories import (
    CountryFactory,
    GoalFactory,
    GoodPracticeExampleFactory,
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


class SectorTestCase(TestCase):
    """Tests for the ``Sector`` model."""
    longMessage = True

    def test_model(self):
        obj = SectorFactory()
        self.assertTrue(obj.pk)

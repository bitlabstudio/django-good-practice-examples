"""Factories for the ``good_practice_examples`` app."""
import factory

from django_libs.tests.factories import HvadFactoryMixin

from ..models import (
    Country,
    Goal,
    GoodPracticeExample,
    Sector,
)


class CountryFactory(factory.DjangoModelFactory):
    """Factory for the ``Country`` model."""
    FACTORY_FOR = Country

    country = 'US'


class GoalFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """Factory for the ``Goal`` model."""
    FACTORY_FOR = Goal

    name = factory.Sequence(lambda n: 'goal name {}'.format(n))


class GoodPracticeExampleFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """Factory for the ``GoodPracticeExample`` model."""
    FACTORY_FOR = GoodPracticeExample

    title = factory.Sequence(lambda n: 'example title {}'.format(n))


class SectorFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """Factory for the ``Sector`` model."""
    FACTORY_FOR = Sector

    name = factory.Sequence(lambda n: 'sector name {}'.format(n))

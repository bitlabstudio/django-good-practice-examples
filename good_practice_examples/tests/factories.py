"""Factories for the ``good_practice_examples`` app."""
import factory

from django_libs.tests.factories import SimpleTranslationMixin

from ..models import (
    Country,
    Goal,
    GoalTranslation,
    GoodPracticeExample,
    GoodPracticeExampleTranslation,
    Sector,
    SectorTranslation,
)


class CountryFactory(factory.Factory):
    """Factory for the ``Country`` model."""
    FACTORY_FOR = Country

    country = 'US'


class BaseGoalFactory(factory.Factory):
    """Factory for the ``Goal`` model."""
    FACTORY_FOR = Goal


class GoalFactory(SimpleTranslationMixin, BaseGoalFactory):
    """Factory for the ``Goal`` model."""
    FACTORY_FOR = Goal

    @staticmethod
    def _get_translation_factory_and_field():
        return (GoalTranslationFactory, 'goal')


class GoalTranslationFactory(factory.Factory):

    """Factory for the ``GoalTranslation`` model."""
    FACTORY_FOR = GoalTranslation

    name = factory.Sequence(lambda n: 'goal name {}'.format(n))
    goal = factory.SubFactory(BaseGoalFactory)
    language = 'en'


class BaseGoodPracticeExampleFactory(factory.Factory):
    """Factory for the ``GoodPracticeExample`` model."""
    FACTORY_FOR = GoodPracticeExample


class GoodPracticeExampleFactory(SimpleTranslationMixin,
                                 BaseGoodPracticeExampleFactory):
    """Factory for the ``GoodPracticeExample`` model."""
    FACTORY_FOR = GoodPracticeExample

    @staticmethod
    def _get_translation_factory_and_field():
        return (GoodPracticeExampleTranslationFactory, 'good_practice_example')


class GoodPracticeExampleTranslationFactory(factory.Factory):

    """Factory for the ``GoodPracticeExampleTranslation`` model."""
    FACTORY_FOR = GoodPracticeExampleTranslation

    title = factory.Sequence(lambda n: 'example title {}'.format(n))
    good_practice_example = factory.SubFactory(BaseGoodPracticeExampleFactory)
    language = 'en'


class BaseSectorFactory(factory.Factory):
    """Factory for the ``Sector`` model."""
    FACTORY_FOR = Sector


class SectorFactory(SimpleTranslationMixin, BaseSectorFactory):
    """Factory for the ``Sector`` model."""
    FACTORY_FOR = Sector

    @staticmethod
    def _get_translation_factory_and_field():
        return (SectorTranslationFactory, 'sector')


class SectorTranslationFactory(factory.Factory):

    """Factory for the ``SectorTranslation`` model."""
    FACTORY_FOR = SectorTranslation

    name = factory.Sequence(lambda n: 'sector name {}'.format(n))
    sector = factory.SubFactory(BaseSectorFactory)
    language = 'en'

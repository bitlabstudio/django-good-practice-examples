"""Models for the ``good_practice_examples`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_countries.fields import CountryField
from django_libs.models_mixins import (
    SimpleTranslationMixin,
    SimpleTranslationPublishedManager,
)
from djangocms_utils.fields import M2MPlaceholderField
from simple_translation.actions import SimpleTranslationPlaceholderActions


class Country(models.Model):
    """
    Contains information about a country specific to a practice.

    :country: Which country the practice took place.

    """
    country = CountryField()

    def __unicode__(self):
        return self.country.code


class Goal(SimpleTranslationMixin, models.Model):
    """
    Holds information about the goal of the practice.

    For translatable fields see ``GoalTranslation``.

    """

    def __unicode__(self):
        return self.get_translation().name


class GoalTranslation(models.Model):
    """
    Holds the translatable fields of the ``Goal`` model.

    :name: Name of the goal.

    """
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=256,
    )
    # needed by simple_translation
    goal = models.ForeignKey(
        'good_practice_examples.Goal',
        verbose_name=_('Goal'),
    )

    language = models.CharField(
        verbose_name=_('Language'),
        max_length=5,
    )


class GoodPracticeExample(SimpleTranslationMixin, models.Model):
    """
    Contains the information about a certain practice.

    For translatable fields see ``GoodPracticeExampleTranslation``.

    :description: The description of the good practice.
    :goals: The goals of this practice.
    :sectors: The sectors of this practice.
    :countries: The countries this practice takes place.

    """
    placeholders = M2MPlaceholderField(
        actions=SimpleTranslationPlaceholderActions(),
        placeholders=('description', ),
    )

    goals = models.ManyToManyField(
        'good_practice_examples.Goal',
        verbose_name=_('Goals'),
    )

    sectors = models.ManyToManyField(
        'good_practice_examples.Sector',
        verbose_name=_('Sectors'),
    )

    countries = models.ManyToManyField(
        'good_practice_examples.Country',
        verbose_name=_('Countries'),
    )

    objects = SimpleTranslationPublishedManager()

    def __unicode__(self):
        return self.get_translation().title


class GoodPracticeExampleTranslation(models.Model):
    """
    Holds the translatable fields of a ``GoodPracticeExample``.

    :title: A short title for the practice.
    :is_published: True, if the practice should show up.

    """
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=256,
    )

    is_published = models.BooleanField(
        verbose_name=_('Is published'),
        default=False,
    )

    #needed by simple_translation
    good_practice_example = models.ForeignKey(
        'good_practice_examples.GoodPracticeExample',
        verbose_name=_('Good practice example'),
    )

    language = models.CharField(
        verbose_name=_('Language'),
        max_length=5,
    )


class Sector(SimpleTranslationMixin, models.Model):
    """
    Holds information about the sector of the practice.

    For translatable fields see ``SectorTranslation``.

    """
    def __unicode__(self):
        return self.get_translation().name


class SectorTranslation(models.Model):
    """
    Holds the translatable fields of the ``Sector`` model.

    :name: Name of the sector.

    """
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=256,
    )

    # needed by simple_translation
    sector = models.ForeignKey(
        'good_practice_examples.Sector',
        verbose_name=_('Sector'),
    )

    language = models.CharField(
        verbose_name=_('Language'),
        max_length=5,
    )

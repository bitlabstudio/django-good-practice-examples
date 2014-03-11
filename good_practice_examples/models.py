"""Models for the ``good_practice_examples`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.fields import PlaceholderField
from django_countries.fields import CountryField
from django_libs.models_mixins import HvadPublishedManager
from hvad.models import TranslatableModel, TranslatedFields


class Country(models.Model):
    """
    Contains information about a country specific to a practice.

    :country: Which country the practice took place.

    """
    country = CountryField()

    def __unicode__(self):
        return self.country.code


class Goal(TranslatableModel):
    """
    Holds information about the goal of the practice.

    """
    translations = TranslatedFields(
        name=models.CharField(
            verbose_name=_('Name'),
            max_length=256,
        )
    )

    def __unicode__(self):
        return self.safe_translation_getter('name', 'Untranslated goal')


class GoodPracticeExample(TranslatableModel):
    """
    Contains the information about a certain practice.

    For translatable fields see ``GoodPracticeExampleTranslation``.

    :description: The description of the good practice.
    :goals: The goals of this practice.
    :sectors: The sectors of this practice.
    :countries: The countries this practice takes place.

    translated:
    :title: A short title for the practice.
    :is_published: True, if the practice should show up.

    """
    practice_description = PlaceholderField(
        'good_practice_example_practice_description',
        related_name='goodpracticeexamples',
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

    translations = TranslatedFields(
        title=models.CharField(
            verbose_name=_('Title'),
            max_length=256,
        ),
        is_published=models.BooleanField(
            verbose_name=_('Is published'),
            default=False,
        )
    )

    objects = HvadPublishedManager()

    def __unicode__(self):
        return self.safe_translation_getter('title', 'Untranslated example')


class Sector(TranslatableModel):
    """
    Holds information about the sector of the practice.

    For translatable fields see ``SectorTranslation``.

    """
    translations = TranslatedFields(
        name=models.CharField(
            verbose_name=_('Name'),
            max_length=256,
        )
    )

    def __unicode__(self):
        return self.safe_translation_getter('name', 'Untranslated sector')

"""Admin classes for the ``good_practice_examples`` app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from multilingual_news.admin import M2MPlaceholderAdmin
from django_libs.admin import MultilingualPublishMixin
from simple_translation.admin import TranslationAdmin

from .models import (
    Country,
    Goal,
    GoodPracticeExample,
    Sector,
)


class GoalAdmin(TranslationAdmin):
    """Admin class for the ``Goal`` model."""
    list_display = ['name', 'languages']

    def name(self, obj):
        return obj.get_translation().name
    name.short_description = _('Name')


class GoodPracticeExampleAdmin(MultilingualPublishMixin, M2MPlaceholderAdmin):
    """Admin class for the ``GoodPracticeExample`` model."""
    list_display = ['title', 'languages', 'is_published']
    list_filter = ('goals', 'sectors', 'countries')

    def title(self, obj):
        return obj.get_translation().title
    title.short_description = _('Title')


class SectorAdmin(TranslationAdmin):
    """Admin class for the ``Sector`` model."""
    list_display = ['name', 'languages']

    def name(self, obj):
        return obj.get_translation().name
    name.short_description = _('Name')


admin.site.register(Country)
admin.site.register(Goal, GoalAdmin)
admin.site.register(GoodPracticeExample, GoodPracticeExampleAdmin)
admin.site.register(Sector, SectorAdmin)

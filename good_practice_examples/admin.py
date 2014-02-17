"""Admin classes for the ``good_practice_examples`` app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from hvad.admin import TranslatableAdmin

from .models import (
    Country,
    Goal,
    GoodPracticeExample,
    Sector,
)


class GoalAdmin(TranslatableAdmin):
    """Admin class for the ``Goal`` model."""
    list_display = ['get_name', 'all_translations']

    def get_name(self, obj):
        return obj.name
    get_name.short_description = _('Name')


class GoodPracticeExampleAdmin(TranslatableAdmin):
    """Admin class for the ``GoodPracticeExample`` model."""
    list_display = ['get_title', 'all_translations', 'get_is_published']
    list_filter = ('goals', 'sectors', 'countries')

    def get_title(self, obj):
        return obj.title
    get_title.short_description = _('Title')

    def get_is_published(self, obj):
        return obj.is_published
    get_is_published.short_description = _('Is published')
    get_is_published.boolean = True


class SectorAdmin(TranslatableAdmin):
    """Admin class for the ``Sector`` model."""
    list_display = ['get_name', 'all_translations']

    def get_name(self, obj):
        return obj.name
    get_name.short_description = _('Name')


admin.site.register(Country)
admin.site.register(Goal, GoalAdmin)
admin.site.register(GoodPracticeExample, GoodPracticeExampleAdmin)
admin.site.register(Sector, SectorAdmin)

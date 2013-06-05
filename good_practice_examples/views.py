"""Views for the ``good_practice_examples`` app."""
from django.views.generic import ListView

from .models import GoodPracticeExample


class GoodPracticeExampleListView(ListView):
    """View to list ``GoodPracticeExample`` objects."""
    model = GoodPracticeExample
    template_name = 'good_practice_examples/examples_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(GoodPracticeExampleListView, self).get_context_data(
            **kwargs)
        countries = []
        goals = []
        sectors = []
        for example in self.object_list:
            countries.extend(example.countries.all())
            goals.extend(example.goals.all())
            sectors.extend(example.sectors.all())
        ctx.update({
            'goals': list(set(goals)),
            'sectors': list(set(sectors)),
            'countries': list(set(countries))})
        return ctx

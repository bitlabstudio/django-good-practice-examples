"""CMS app-hook for the ``good_practice_examples`` app."""
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class GoodPracticeExamplesApphook(CMSApp):
    name = _("Good practice examples")
    urls = ["good_practice_examples.urls"]

apphook_pool.register(GoodPracticeExamplesApphook)

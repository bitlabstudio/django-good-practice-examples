"""Registering translated models for the ``good_practice_examples`` app."""
from simple_translation.translation_pool import translation_pool

from . import models


translation_pool.register_translation(models.Goal, models.GoalTranslation)
translation_pool.register_translation(
    models.GoodPracticeExample, models.GoodPracticeExampleTranslation)
translation_pool.register_translation(models.Sector, models.SectorTranslation)

# flake8: noqa
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

class Migration(DataMigration):

    depends_on = (
        ('cms', '0058_placeholderref_table_rename'),
    )

    def migrate_placeholder(self, orm, goodpracticeexample, old_slot, new_slot,
                            new_field):
        placeholder = None
        try:
            placeholder_m2m_object = goodpracticeexample.placeholders.through.objects.get(
                goodpracticeexample=goodpracticeexample, placeholder__slot=old_slot)
            placeholder = placeholder_m2m_object.placeholder
        except ObjectDoesNotExist:
            pass

        if placeholder:
            new_placeholder = orm['cms.Placeholder'].objects.create(
                slot=new_slot)
            for plugin in placeholder.get_plugins():
                plugin.placeholder_id = new_placeholder.pk
                plugin.save()
            setattr(goodpracticeexample, new_field, new_placeholder)
            goodpracticeexample.save()
            try:
                placeholder_m2m_object.delete()
                placeholder.delete()
            except ObjectDoesNotExist:
                pass

    def forwards(self, orm):
        for goodpracticeexample in orm['good_practice_examples.GoodPracticeExample'].objects.all():
            self.migrate_placeholder(
                orm, goodpracticeexample, 'practice_description', 'good_practice_example_practice_description',
                'practice_description')


    def backwards(self, orm):
        raise RuntimeError('No backwards migration provided.')

    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'good_practice_examples.country': {
            'Meta': {'object_name': 'Country'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'good_practice_examples.goal': {
            'Meta': {'object_name': 'Goal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'good_practice_examples.goaltranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'GoalTranslation', 'db_table': "u'good_practice_examples_goal_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['good_practice_examples.Goal']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'good_practice_examples.goodpracticeexample': {
            'Meta': {'object_name': 'GoodPracticeExample'},
            'countries': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['good_practice_examples.Country']", 'symmetrical': 'False'}),
            'goals': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['good_practice_examples.Goal']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'placeholders': ('djangocms_utils.fields.M2MPlaceholderField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'practice_description': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'goodpracticeexamples'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'sectors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['good_practice_examples.Sector']", 'symmetrical': 'False'})
        },
        u'good_practice_examples.goodpracticeexampletranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'GoodPracticeExampleTranslation', 'db_table': "u'good_practice_examples_goodpracticeexample_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['good_practice_examples.GoodPracticeExample']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'good_practice_examples.sector': {
            'Meta': {'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'good_practice_examples.sectortranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'SectorTranslation', 'db_table': "u'good_practice_examples_sector_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['good_practice_examples.Sector']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['good_practice_examples']
    symmetrical = True

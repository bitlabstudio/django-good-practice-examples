# flake8: noqa
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'GoodPracticeExample.practice_description'
        db.add_column(u'good_practice_examples_goodpracticeexample', 'practice_description',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='goodpracticeexamples', null=True, to=orm['cms.Placeholder']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'GoodPracticeExample.practice_description'
        db.delete_column(u'good_practice_examples_goodpracticeexample', 'practice_description_id')


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

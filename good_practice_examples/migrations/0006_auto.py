# flake8: noqa
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field placeholders on 'GoodPracticeExample'
        db.delete_table(db.shorten_name(u'good_practice_examples_goodpracticeexample_placeholders'))


    def backwards(self, orm):
        # Adding M2M table for field placeholders on 'GoodPracticeExample'
        m2m_table_name = db.shorten_name(u'good_practice_examples_goodpracticeexample_placeholders')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('goodpracticeexample', models.ForeignKey(orm[u'good_practice_examples.goodpracticeexample'], null=False)),
            ('placeholder', models.ForeignKey(orm['cms.placeholder'], null=False))
        ))
        db.create_unique(m2m_table_name, ['goodpracticeexample_id', 'placeholder_id'])


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

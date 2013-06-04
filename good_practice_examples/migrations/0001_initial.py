# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'good_practice_examples_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
        ))
        db.send_create_signal(u'good_practice_examples', ['Country'])

        # Adding model 'Goal'
        db.create_table(u'good_practice_examples_goal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'good_practice_examples', ['Goal'])

        # Adding model 'GoalTranslation'
        db.create_table(u'good_practice_examples_goaltranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('goal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['good_practice_examples.Goal'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'good_practice_examples', ['GoalTranslation'])

        # Adding model 'GoodPracticeExample'
        db.create_table(u'good_practice_examples_goodpracticeexample', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'good_practice_examples', ['GoodPracticeExample'])

        # Adding M2M table for field placeholders on 'GoodPracticeExample'
        m2m_table_name = db.shorten_name(u'good_practice_examples_goodpracticeexample_placeholders')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('goodpracticeexample', models.ForeignKey(orm[u'good_practice_examples.goodpracticeexample'], null=False)),
            ('placeholder', models.ForeignKey(orm['cms.placeholder'], null=False))
        ))
        db.create_unique(m2m_table_name, ['goodpracticeexample_id', 'placeholder_id'])

        # Adding M2M table for field goals on 'GoodPracticeExample'
        m2m_table_name = db.shorten_name(u'good_practice_examples_goodpracticeexample_goals')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('goodpracticeexample', models.ForeignKey(orm[u'good_practice_examples.goodpracticeexample'], null=False)),
            ('goal', models.ForeignKey(orm[u'good_practice_examples.goal'], null=False))
        ))
        db.create_unique(m2m_table_name, ['goodpracticeexample_id', 'goal_id'])

        # Adding M2M table for field sectors on 'GoodPracticeExample'
        m2m_table_name = db.shorten_name(u'good_practice_examples_goodpracticeexample_sectors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('goodpracticeexample', models.ForeignKey(orm[u'good_practice_examples.goodpracticeexample'], null=False)),
            ('sector', models.ForeignKey(orm[u'good_practice_examples.sector'], null=False))
        ))
        db.create_unique(m2m_table_name, ['goodpracticeexample_id', 'sector_id'])

        # Adding M2M table for field countries on 'GoodPracticeExample'
        m2m_table_name = db.shorten_name(u'good_practice_examples_goodpracticeexample_countries')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('goodpracticeexample', models.ForeignKey(orm[u'good_practice_examples.goodpracticeexample'], null=False)),
            ('country', models.ForeignKey(orm[u'good_practice_examples.country'], null=False))
        ))
        db.create_unique(m2m_table_name, ['goodpracticeexample_id', 'country_id'])

        # Adding model 'GoodPracticeExampleTranslation'
        db.create_table(u'good_practice_examples_goodpracticeexampletranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('good_practice_example', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['good_practice_examples.GoodPracticeExample'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'good_practice_examples', ['GoodPracticeExampleTranslation'])

        # Adding model 'Sector'
        db.create_table(u'good_practice_examples_sector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'good_practice_examples', ['Sector'])

        # Adding model 'SectorTranslation'
        db.create_table(u'good_practice_examples_sectortranslation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['good_practice_examples.Sector'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'good_practice_examples', ['SectorTranslation'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'good_practice_examples_country')

        # Deleting model 'Goal'
        db.delete_table(u'good_practice_examples_goal')

        # Deleting model 'GoalTranslation'
        db.delete_table(u'good_practice_examples_goaltranslation')

        # Deleting model 'GoodPracticeExample'
        db.delete_table(u'good_practice_examples_goodpracticeexample')

        # Removing M2M table for field placeholders on 'GoodPracticeExample'
        db.delete_table(db.shorten_name(u'good_practice_examples_goodpracticeexample_placeholders'))

        # Removing M2M table for field goals on 'GoodPracticeExample'
        db.delete_table(db.shorten_name(u'good_practice_examples_goodpracticeexample_goals'))

        # Removing M2M table for field sectors on 'GoodPracticeExample'
        db.delete_table(db.shorten_name(u'good_practice_examples_goodpracticeexample_sectors'))

        # Removing M2M table for field countries on 'GoodPracticeExample'
        db.delete_table(db.shorten_name(u'good_practice_examples_goodpracticeexample_countries'))

        # Deleting model 'GoodPracticeExampleTranslation'
        db.delete_table(u'good_practice_examples_goodpracticeexampletranslation')

        # Deleting model 'Sector'
        db.delete_table(u'good_practice_examples_sector')

        # Deleting model 'SectorTranslation'
        db.delete_table(u'good_practice_examples_sectortranslation')


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
            'Meta': {'object_name': 'GoalTranslation'},
            'goal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['good_practice_examples.Goal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'good_practice_examples.goodpracticeexample': {
            'Meta': {'object_name': 'GoodPracticeExample'},
            'countries': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['good_practice_examples.Country']", 'symmetrical': 'False'}),
            'goals': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['good_practice_examples.Goal']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'placeholders': ('djangocms_utils.fields.M2MPlaceholderField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'sectors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['good_practice_examples.Sector']", 'symmetrical': 'False'})
        },
        u'good_practice_examples.goodpracticeexampletranslation': {
            'Meta': {'object_name': 'GoodPracticeExampleTranslation'},
            'good_practice_example': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['good_practice_examples.GoodPracticeExample']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'good_practice_examples.sector': {
            'Meta': {'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'good_practice_examples.sectortranslation': {
            'Meta': {'object_name': 'SectorTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['good_practice_examples.Sector']"})
        }
    }

    complete_apps = ['good_practice_examples']

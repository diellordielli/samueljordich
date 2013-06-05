# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'News', fields ['featured']
        db.delete_unique(u'news_news', ['featured'])


    def backwards(self, orm):
        # Adding unique constraint on 'News', fields ['featured']
        db.create_unique(u'news_news', ['featured'])


    models = {
        u'cartoons.cartoon': {
            'Meta': {'object_name': 'Cartoon'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category'", 'blank': 'True', 'to': u"orm['cartoons.Category']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'cartoons.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'news.news': {
            'Meta': {'ordering': "['date']", 'object_name': 'News'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'news'", 'blank': 'True', 'to': u"orm['cartoons.Cartoon']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['news']
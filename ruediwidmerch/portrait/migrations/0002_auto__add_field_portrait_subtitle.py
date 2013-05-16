# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Portrait.subtitle'
        db.add_column(u'portrait_portrait', 'subtitle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Portrait.subtitle'
        db.delete_column(u'portrait_portrait', 'subtitle')


    models = {
        u'cartoons.cartoon': {
            'Meta': {'object_name': 'Cartoon'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category'", 'blank': 'True', 'to': u"orm['cartoons.Category']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'cartoons.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'portrait.portrait': {
            'Meta': {'object_name': 'Portrait'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'portraits'", 'blank': 'True', 'to': u"orm['cartoons.Cartoon']"}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['portrait']
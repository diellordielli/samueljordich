# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Portrait'
        db.create_table(u'portrait_portrait', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('width', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'portrait', ['Portrait'])

        # Adding M2M table for field images on 'Portrait'
        db.create_table(u'portrait_portrait_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('portrait', models.ForeignKey(orm[u'portrait.portrait'], null=False)),
            ('cartoon', models.ForeignKey(orm[u'cartoons.cartoon'], null=False))
        ))
        db.create_unique(u'portrait_portrait_images', ['portrait_id', 'cartoon_id'])


    def backwards(self, orm):
        # Deleting model 'Portrait'
        db.delete_table(u'portrait_portrait')

        # Removing M2M table for field images on 'Portrait'
        db.delete_table('portrait_portrait_images')


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['portrait']
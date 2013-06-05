# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'news_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False, unique=True)),
        ))
        db.send_create_signal(u'news', ['News'])

        # Adding M2M table for field images on 'News'
        db.create_table(u'news_news_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('news', models.ForeignKey(orm[u'news.news'], null=False)),
            ('cartoon', models.ForeignKey(orm[u'cartoons.cartoon'], null=False))
        ))
        db.create_unique(u'news_news_images', ['news_id', 'cartoon_id'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'news_news')

        # Removing M2M table for field images on 'News'
        db.delete_table('news_news_images')


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
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'news'", 'blank': 'True', 'to': u"orm['cartoons.Cartoon']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['news']
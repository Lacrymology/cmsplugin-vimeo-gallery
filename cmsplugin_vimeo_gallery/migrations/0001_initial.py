# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VimeoVideo'
        db.create_table('cmsplugin_vimeo_gallery_vimeovideo', (
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('thumbnail_large', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('thumbnail_medium', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('thumbnail_small', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('cmsplugin_vimeo_gallery', ['VimeoVideo'])


    def backwards(self, orm):
        # Deleting model 'VimeoVideo'
        db.delete_table('cmsplugin_vimeo_gallery_vimeovideo')


    models = {
        'cmsplugin_vimeo_gallery.vimeovideo': {
            'Meta': {'object_name': 'VimeoVideo'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'thumbnail_large': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'thumbnail_medium': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'thumbnail_small': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_vimeo_gallery']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VideoGallery'
        db.create_table('cmsplugin_vimeo_gallery_videogallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('template', self.gf('django.db.models.fields.CharField')(default='cmsplugin_vimeo_gallery/gallery/gallery.html', max_length=255)),
        ))
        db.send_create_signal('cmsplugin_vimeo_gallery', ['VideoGallery'])

        # Adding M2M table for field videos on 'VideoGallery'
        db.create_table('cmsplugin_vimeo_gallery_videogallery_videos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('videogallery', models.ForeignKey(orm['cmsplugin_vimeo_gallery.videogallery'], null=False)),
            ('vimeovideo', models.ForeignKey(orm['cmsplugin_vimeo_gallery.vimeovideo'], null=False))
        ))
        db.create_unique('cmsplugin_vimeo_gallery_videogallery_videos', ['videogallery_id', 'vimeovideo_id'])


    def backwards(self, orm):
        # Deleting model 'VideoGallery'
        db.delete_table('cmsplugin_vimeo_gallery_videogallery')

        # Removing M2M table for field videos on 'VideoGallery'
        db.delete_table('cmsplugin_vimeo_gallery_videogallery_videos')


    models = {
        'cmsplugin_vimeo_gallery.videogallery': {
            'Meta': {'object_name': 'VideoGallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'cmsplugin_vimeo_gallery/gallery/gallery.html'", 'max_length': '255'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cmsplugin_vimeo_gallery.VimeoVideo']", 'symmetrical': 'False'})
        },
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
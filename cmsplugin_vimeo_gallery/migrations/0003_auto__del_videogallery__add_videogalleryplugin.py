# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'VideoGallery'
        db.delete_table('cmsplugin_vimeo_gallery_videogallery')

        # Removing M2M table for field videos on 'VideoGallery'
        db.delete_table('cmsplugin_vimeo_gallery_videogallery_videos')

        # Adding model 'VideoGalleryPlugin'
        db.create_table('cmsplugin_videogalleryplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('template', self.gf('django.db.models.fields.CharField')(default='cmsplugin_vimeo_gallery/gallery/gallery.html', max_length=255)),
        ))
        db.send_create_signal('cmsplugin_vimeo_gallery', ['VideoGalleryPlugin'])

        # Adding M2M table for field videos on 'VideoGalleryPlugin'
        db.create_table('cmsplugin_vimeo_gallery_videogalleryplugin_videos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('videogalleryplugin', models.ForeignKey(orm['cmsplugin_vimeo_gallery.videogalleryplugin'], null=False)),
            ('vimeovideo', models.ForeignKey(orm['cmsplugin_vimeo_gallery.vimeovideo'], null=False))
        ))
        db.create_unique('cmsplugin_vimeo_gallery_videogalleryplugin_videos', ['videogalleryplugin_id', 'vimeovideo_id'])


    def backwards(self, orm):
        # Adding model 'VideoGallery'
        db.create_table('cmsplugin_vimeo_gallery_videogallery', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.CharField')(default='cmsplugin_vimeo_gallery/gallery/gallery.html', max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('cmsplugin_vimeo_gallery', ['VideoGallery'])

        # Adding M2M table for field videos on 'VideoGallery'
        db.create_table('cmsplugin_vimeo_gallery_videogallery_videos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('videogallery', models.ForeignKey(orm['cmsplugin_vimeo_gallery.videogallery'], null=False)),
            ('vimeovideo', models.ForeignKey(orm['cmsplugin_vimeo_gallery.vimeovideo'], null=False))
        ))
        db.create_unique('cmsplugin_vimeo_gallery_videogallery_videos', ['videogallery_id', 'vimeovideo_id'])

        # Deleting model 'VideoGalleryPlugin'
        db.delete_table('cmsplugin_videogalleryplugin')

        # Removing M2M table for field videos on 'VideoGalleryPlugin'
        db.delete_table('cmsplugin_vimeo_gallery_videogalleryplugin_videos')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 23, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_vimeo_gallery.videogalleryplugin': {
            'Meta': {'object_name': 'VideoGalleryPlugin', 'db_table': "'cmsplugin_videogalleryplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
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
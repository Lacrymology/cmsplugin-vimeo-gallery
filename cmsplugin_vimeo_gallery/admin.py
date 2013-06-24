# -*- coding: utf-8 -*-

"""
.. module:: cmsplugin_vimeo_gallery.admin
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""

from django.contrib import admin
from cmsplugin_vimeo_gallery import models

class VimeoVideoAdmin(admin.ModelAdmin):
    readonly_fields = ['title', 'description',
                       'thumbnail_large', 'thumbnail_medium', 'thumbnail_small']

admin.site.register(models.VimeoVideo, VimeoVideoAdmin)

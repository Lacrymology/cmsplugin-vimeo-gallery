# -*- coding: utf-8 -*-

"""
.. module:: cmsplugin_vimeo_gallery.cms_plugins
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_vimeo_gallery import models

class CMSVimeoGalleryPlugin(CMSPluginBase):

    model = models.VideoGalleryPlugin
    filter_horizontal = ['videos', ]
    name = _('Vimeo gallery')
    render_template = 'cmsplugin_vimeo_gallery/gallery.html'

    def render(self, context, instance, placeholder):
        context.update({
                        'videos': instance.videos.all(),
                        'gallery': instance,
                       })
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(CMSVimeoGalleryPlugin)

# -*- coding: utf-8 -*-

"""
.. module:: cmsplugin_vimeo_gallery.models
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
from django.core.exceptions import ValidationError
from os import path
import threading
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

from cmsplugin_vimeo_gallery import utils
from cmsplugin_vimeo_gallery import api

localdata = threading.local()
localdata.TEMPLATE_CHOICES = utils.autodiscover_templates()
TEMPLATE_CHOICES = localdata.TEMPLATE_CHOICES

class VimeoVideo(models.Model):
    """
    A single video in the gallery
    """
    id = models.PositiveIntegerField(_('id'), blank=True, primary_key=True)
    url = models.CharField(_("url"), max_length=128, blank=True,
                           help_text=_("Please enter the video's numerical ID "
                                       "or URL"))
    title = models.CharField(_('title'), max_length=128, blank=True,
                             editable=False)
    description = models.TextField(_('description'), blank=True)
    thumbnail_large = models.CharField(_("thumbnail large"), max_length=128,
                                       editable=False)
    thumbnail_medium = models.CharField(_("thumbnail medium"), max_length=128,
                                        editable=False)
    thumbnail_small = models.CharField(_("thumbnail small"), max_length=128,
                                       editable=False)

    class Meta:
        verbose_name = _('vimeo video')
        verbose_name_plural = _('vimeo videos')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not (self.id or self.url):
            raise ValidationError, _("You need to provide either the id or the "
                                     "URL")
        id = self.id or path.basename(self.url)
        video_info = api.get_video_info(id)
        self.id = video_info['id']
        self.url = video_info['url']
        self.title = video_info['title']
        self.description = video_info['description']
        self.thumbnail_large = video_info['thumbnail_large']
        self.thumbnail_medium = video_info['thumbnail_medium']
        self.thumbnail_small = video_info['thumbnail_small']
        return super(VimeoVideo, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"{} ({})".format(self.title, self.id)

class VideoGalleryPlugin(CMSPlugin):
    """
    Video Gallery
    <iframe src="http://player.vimeo.com/video/VIDEO_ID" width="WIDTH" height="HEIGHT" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
    Parameters

    Here is a list of all the parameters that can be used with the Universal Player. They should be added as query parameters to the src of the iframe.

    title       Show the title on the video. Defaults to 1.
    byline      Show the user’s byline on the video. Defaults to 1.
    portrait    Show the user’s portrait on the video. Defaults to 1.
    color       Specify the color of the video controls. Defaults to 00adef.
                Make sure that you don’t include the #.
    autoplay    Play the video automatically on load. Defaults to 0. Note that
                this won’t work on some devices.
    loop        Play the video again when it reaches the end. Defaults to 0.
    api         Set to 1 to enable the Javascript API.
    player_id   An unique id for the player that will be passed back with all
                Javascript API responses.
    """
    name = models.CharField(_('name'), max_length=32)
    slug = models.SlugField(_('slug'))
    template = models.CharField(
        max_length=255,
        choices=TEMPLATE_CHOICES,
        default='cmsplugin_vimeo_gallery/gallery.html',
    )
    videos = models.ManyToManyField(verbose_name=_('videos'), to=VimeoVideo,
                                    null=True, blank=True)

    class Meta:
        verbose_name = _('video gallery')
        verbose_name_plural = _('video galleries')

    def __unicode__(self):
        return u"{} ({})".format(self.name, self.videos.count())

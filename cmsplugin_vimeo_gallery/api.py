# -*- coding: utf-8 -*-

"""
.. module:: 
   :platform: Unix
   :synopsis: TODO

.. moduleauthor:: Tomas Neme <lacrymology@gmail.com>

"""
import requests
from django.core.cache import cache
from django.core.serializers.json import simplejson

ENDPOINT = "http://vimeo.com/api/v2/"
VIDEO_ENDPOINT = "%svideo/{video}.json" % ENDPOINT

def get_video_info(video_id):
    """
    Return a dict with the info of a given video
    :param video_id: the vimeo video ID
    :return: a dict object with the data described at
    """
    cache_key = "vimeo-video-id-{}".format(video_id)
    info = cache.get(cache_key)
    if info is not None:
        return info
    res = requests.get(VIDEO_ENDPOINT.format(video=video_id))
    if not res.ok:
        res.raise_for_status()
    info = simplejson.loads(res.content)[0]
    cache.set(cache_key, info)
    return info

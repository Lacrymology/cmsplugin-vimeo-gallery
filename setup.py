#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin-vimeo-gallery',
    version='0.0.0',
    author='Tomas Neme',
    author_email='lacrymology@gmail.com',
    url='http://github.com/Lacrymology',
    description = 'DjangoCMS vimeo embedded video gallery plugin with '
                  'drag&drop reordering in admin',
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        ],
    package_data={
        'cmsplugin_vimeo_gallery': [
            'templates/cmsplugin_vimeo_gallery/*.html',
            'static/js/*.js'
        ]
    },
)

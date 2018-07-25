# coding: utf-8

from __future__ import unicode_literals
from functools import partial
import json

from .base_object import BaseObject
from boxsdk.config import API

class MetadataTemplateUpdate(object):
    """
    Helper class for updating Box metadata template.
    See https://developer.box.com/v2.0/reference#metadata-templates for more details.
    """
    def __init__(self):
        self._ops = []

    @property
    def ops(self):
        """
        Get a list of json update operations in this update.

        :return:
            The list of json update operations in this update.
        :rtype:
            `list` of `dict`
        """
        return self._ops

    def addEnumOptions(self, field_key, option_key):
        """
        Insert an add operation to this metadata update.

        :param path:
            JSON pointer specifying where to add the new value.
        :type path:
            `unicode`
        :param value:
            The value to add to the metadata document.
        :type value:
            `unicode`
        """
        data = {
            'op': 'addEmumOption',
            'field_key': field_key,
            'data': {
                'key': option_key,
            }
        }
        self._ops.append(data)

class MetadataTemplate(BaseObject):
    """Represents a Box metadata template."""

    _item_type = 'metadata_template'

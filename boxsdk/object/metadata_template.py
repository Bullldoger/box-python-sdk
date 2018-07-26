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

    def add_enum_options(self, field_key, option_key):
        """
        Insert an add enum operation to this metadata update.

        :param field_key:
            The key of the field to add the enum option.
        :type field_key:
            `unicode`
        :param option_key:
            The enum option
        :type option_key:
            `unicode`
        """
        data = {
            'op': 'addEmumOption',
            'fieldKey': field_key,
            'data': {
                'key': option_key,
            }
        }
        self._ops.append(data)

    def add_field(self, display_name, option_key, is_hidden, field_type):
        """
        Insert an add field operation to this metadata update.

        :param display_name:
            The display name for the template.
        :type display_name:
            `unicode`
        :param option_key:
            The value to add to the metadata document.
        :type option_key:
            `unicode`
        """
        data = {
            'op': 'addField',
            'data': {
                'displayName': display_name,
                'key': option_key,
                'hidden': is_hidden,
                'type': field_type
            }
        }
        self._ops.append(data)


    def edit_field(self, display_name=None, is_hidden=None, description=None, field_key=None):
        """
         Edits any number of the base properties of a field: displayName, hidden, description, key.

        :param display_name:
            The display name for the template.
        :type display_name:
            `unicode`
        :param field_key:
            The key of the field to be edited.
        :type field_key:
            `unicode`
        :param description:
            The description of the metadata template.
        :type description:
            `unicode`
        :param is_hidden:
            Indicates whether the field is hidden.
        :type is_hidden:
            `boolean`
        """
        data = {
            'op': 'editField',
            'field_key': field_key,
            'data': {
                'displayName': display_name,
                'hidden': is_hidden,
                'description': description
            }
        }
        self._ops.append(data)


    def edit_template(self, display_name, is_hidden):
        data = {
            'op': 'editTemplate',
            'data': {
                'displayName': display_name,
                'hidden': is_hidden
            }
        }
        self._ops.append(data)


    def reorder_enum_options(self, field_key, option_keys):
        """
        Reorders the enum option list to match the requested enum option list.

        :param field_key:
            The key of the field to reorder enum options. Must refer to an enum field.
        :type field_key:
            `unicode`
        :param option_keys:
            The new list of enum option keys in the requested order.
        :type option_keys:
            `list`
        """
        data = {
            'op': 'reorderEnumOptions',
            'fieldKey': field_key,
            'enumOptionKeys': option_keys
        }
        self._ops.append(data)


    def reorder_fields(self, field_keys):
        """
        Reorders the enum option list to match the requested enum option list.

        :param field_key:
            The new list of field keys in the requested order.
        :type field_key:
            `list`
        """
        data = {
            'op': 'reorderFields',
            'fieldKey': field_keys,
        }
        self._ops.append(data)


    def edit_enum_option(self, field_key, option_key, new_key):
        """
        Edits the enumOption.

        :param field_key:
            The key of the field the specified enum option belongs to. Must refer to an enum field.
        :type field_key:
            `unicode`
        :param option_key:
            The key of the enum option to be edited.
        :type option_key:
            `unicode`
        :param new_key:
            The new key of the enumOption.
        :type new_key:
            `unicode`
        """
        data = {
            'op': 'editEnumOption',
            'fieldKey': field_key,
            'enumOptionKey': option_key,
            'data': {
                'key': new_key
            }
        }
        self._ops.append(data)


    def remove_enum_option(self, field_key, option_key):
        """
        Removes the specified enum option from the specified enum field.

        :param field_key:
            The key of the field to be removed.
        :type field_key:
            `unicode`
        :param option_key:
            The key of the field from which the enum option should be removed. Must refer to an enum field.
        :type option_key:
            `unicode`
        """
        data = {
            'op': 'removeEnumOption',
            'fieldKey': field_key,
            'enumOptionKey': option_key
        }
        self._ops.append(data)


    def remove_field(self, field_key):
        """
        Removes the specified field from the template.

        :param field_key:
            The key of the field to be removed.
        :type field_key:
            `unicode`
        """
        data = {
            'op': 'removeField',
            'fieldKey': field_key
        }
        self._ops.append(data)


class MetadataTemplate(BaseObject):
    """Represents a Box metadata template."""

    _item_type = 'metadata_template'

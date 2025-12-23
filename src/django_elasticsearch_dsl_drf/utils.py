"""
Utils.
"""

import datetime

from elasticsearch.dsl.search_base import EmptySearch


class DictionaryProxy(object):
    """Dictionary proxy."""

    def __init__(self, mapping, meta=None):
        self.__mapping = mapping
        self.meta = meta

    def __getattr__(self, item):
        if item == "meta":
            return self.meta
        val = self.__mapping.get(item, None)
        if isinstance(val, datetime.datetime) and not val.tzinfo:
            val = val.date()
        return val

    def to_dict(self):
        """To dict.

        :return:
        """
        return self.__mapping

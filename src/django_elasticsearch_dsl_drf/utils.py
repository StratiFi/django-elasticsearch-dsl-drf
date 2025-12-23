"""
Utils.
"""

import datetime

from elasticsearch.dsl.search import EmptySearch


__title__ = "django_elasticsearch_dsl_drf.utils"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2017-2020 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = (
    "DictionaryProxy",
    "EmptySearch",
)


class DictionaryProxy:
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

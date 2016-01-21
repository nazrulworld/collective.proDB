# -*- coding: utf-8 -*-
# ++ This file `sqlite.py` is generated at 1/11/16 6:30 PM ++
import zope.interface
from collective.proDB.interfaces import IFakeObject
from collective.proDB.interfaces import IProdDBConnection
from collective.proDB import _
try:
    import sqlite3
except ImportError:
    try:
        from pysqlite2 import dbapi2 as sqlite3
    except ImportError:
        sqlite3 = IFakeObject

__author__ = "Md Nazrul Islam<connect2nazrul@gmail.com>"


@zope.interface.implementer(IProdDBConnection)
class DBConnection(object):
    """  """

    def __init__(self, db_name, timeout=5.0, factory=None, **kwargs):
        """
        :param db_name:
        :return:
        """
        self.__storage__ = dict()
        self.db_name = db_name

        if 'timeout' not in kwargs.keys():
            kwargs.update({'timeout': timeout})

        if 'factory' not in kwargs.keys():
             kwargs.update({'factory': factory})

        self.__storage__['connection'] = self._connect(db_name, **kwargs)

    def _connect(self, db_name=None, **kwargs):

        """
        :param db_name:
        :return:
        """
        db_name = db_name or self.db_name
        try:
            connection = sqlite3.connect(db_name, **kwargs)
        except sqlite3.DatabaseError:
            raise
        except sqlite3.Error:
            raise
        except TypeError:

            if sqlite3 is IFakeObject:
                raise ImportError(_("You must install sqlite3 extensions. "
                                    "More https://pysqlite.readthedocs.org/en/latest/sqlite3.html"))

            raise
        else:
            return connection

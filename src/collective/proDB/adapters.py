# -*- coding: utf-8 -*-
# ++ This file `adapters.py` is generated at 1/10/16 7:28 PM ++
import zope.interface
from zope.component import adapts
from zope.component import getUtility
from Products.CMFCore.interfaces import ISiteRoot
from .interfaces import IProdDBConnection
from .interfaces import IProdDBConnectionManagerAdapter
from .metaconfigure import local_db_manager
from plone.memoize import instance

__author__ = "Md Nazrul Islam<connect2nazrul@gmail.com>"


@zope.interface.implementer(IProdDBConnectionManagerAdapter)
class ProdDBConnectionManagerAdapter(object):

    """
    """
    adapts(ISiteRoot)

    def __init__(self, portal):

        """
        :param portal:
        :return:
        """
        self.context = portal

    @instance.memoize
    def _db(self, connection_name, force=0):
        """
        :param connection_name:
        :param force:
        :return:
        """

        connection_instance = getUtility(IProdDBConnection, name=connection_name)
        return connection_instance

    def get_db(self, connection_name=None):

        connection_name = connection_name or local_db_manager.default

        return self._db(connection_name)

    def query(self):
        pass

    def fetchall(self):
        pass

    def fetchone(self):
        pass

    def first(self):
        pass

    def last(self):
        pass

    def filter(self):
        pass


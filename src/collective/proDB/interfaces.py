# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
import zope.schema
import zope.interface
import zope.configuration.fields
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from collective.proDB import _


class ICollectiveProdbLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IProdDBConnection(zope.interface.Interface):

    """  """

    def _connect(self, *args, **kwargs):
        raise NotImplementedError('')

    def _cursor(self, dict_type=None):
        raise NotImplementedError('')

    def _execute(self, statement, cursor):
        raise NotImplementedError('')

    def _fetch_all(self, statement, cursor=None):
        pass

    def _fetch_one(self, statement, cursor=None):
        raise NotImplementedError('')

    def _connection_close(self, connection):
        raise NotImplementedError('')

    def _clean(self):
        """ Close active cursors, connection """
        pass


class IProdDBConnectionManger(zope.interface.Interface):

    """  """


class IProdDBConnectionManagerAdapter(zope.interface.Interface):

    """  """


class IProDatabaseTool(zope.interface.Interface):
    """ """


class IFakeObject(object):
    pass

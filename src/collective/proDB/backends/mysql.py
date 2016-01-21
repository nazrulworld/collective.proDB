# -*- coding: utf-8 -*-
# ++ This file `mysql.py` is generated at 1/11/16 6:30 PM ++
import zope.interface
from collective.proDB.interfaces import IFakeObject
from collective.proDB.interfaces import IProdDBConnection
from collective.proDB import _
try:
    import MySQLdb
except ImportError:
    MySQLdb = IFakeObject

__author__ = "Md Nazrul Islam<connect2nazrul@gmail.com>"


@zope.interface.implementer(IProdDBConnection)
class DBConnection(object):

    def __init__(self):
        pass

    def _connect(self):
        pass


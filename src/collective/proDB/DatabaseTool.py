# -*- coding: utf-8 -*-
# ++ This file `DatabaseTool.py` is generated at 1/19/16 6:38 PM ++
import zope.interface
from AccessControl import ClassSecurityInfo
from Products.CMFPlone.PloneBaseTool import PloneBaseTool
from .interfaces import IProDatabaseTool

__author__ = "Md Nazrul Islam<connect2nazrul@gmail.com>"


@zope.interface.implementer(IProDatabaseTool)
class ProDatabaseTool(PloneBaseTool):
    """

    """
    meta_type = 'Pro Database Tool'
    toolicon = ''
    security = ClassSecurityInfo()



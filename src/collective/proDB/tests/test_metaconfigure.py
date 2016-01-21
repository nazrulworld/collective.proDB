# -*- coding: utf-8 -*-
# ++ This file `test_metaconfigure.py` is generated at 1/20/16 8:10 PM ++
try:
    import unittest2 as unittest
except ImportError:
    import unittest
from zope.component import queryUtility

from collective.proDB.interfaces import IProdDBConnection
from collective.proDB.metaconfigure import generate_id
from collective.proDB.testing import COLLECTIVE_PRODB_INTEGRATION_TESTING

__author__ = "Md Nazrul Islam<connect2nazrul@gmail.com>"


class TestProDBConfiguration(unittest.TestCase):
    """
    """
    layer = COLLECTIVE_PRODB_INTEGRATION_TESTING

    def setUp(self):
        """
        :return:
        """
        super(TestProDBConfiguration, self)
        self.portal = self.layer['portal']

    def test_configure_registered(self):
        """
        :return:
        """
        db_connection = queryUtility(IProdDBConnection, name=generate_id('demo_connection', self.portal, duplicate_constraint=False))

        self.assertIsNotNone(db_connection)

# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.proDB.testing import COLLECTIVE_PRODB_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.proDB is properly installed."""

    layer = COLLECTIVE_PRODB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.proDB is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.proDB'))

    def test_browserlayer(self):
        """Test that ICollectiveProdbLayer is registered."""
        from collective.proDB.interfaces import (
            ICollectiveProdbLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveProdbLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_PRODB_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.proDB'])

    def test_product_uninstalled(self):
        """Test if collective.proDB is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.proDB'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveProdbLayer is removed."""
        from collective.proDB.interfaces import ICollectiveProdbLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveProdbLayer, utils.registered_layers())

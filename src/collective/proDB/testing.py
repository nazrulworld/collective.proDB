# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig
import collective.proDB

configure_zcml = """
<configure
    xmlns="http://namespaces.zope.org/zope"
    xmlns:i18n="http://namespaces.zope.org/i18n"
    xmlns:prodb="http://namespaces.zope.org/prodb"
    i18n_domain="collective.proDB">
  <prodb:configuration name="demo_connection">
    <prodb:database
      name="/tmp/test_db.db"
      dbms="sqlite"
      charset="utf8"
    />
  </prodb:configuration>
</configure>
"""


class CollectiveProdbLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):

        """
        :param app:
        :param configurationContext:
        :return:
        """
        # load meta first
        xmlconfig.file('meta.zcml', package=collective.proDB, context=configurationContext)
        self.loadZCML(package=collective.proDB)
        # Extra configuration, only applicable for testing
        xmlconfig.string(configure_zcml, configurationContext)

    def setUpPloneSite(self, portal):
        """
        :param portal:
        :return:
        """
        applyProfile(portal, 'collective.proDB:default')


COLLECTIVE_PRODB_FIXTURE = CollectiveProdbLayer()


COLLECTIVE_PRODB_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PRODB_FIXTURE,),
    name='CollectiveProdbLayer:IntegrationTesting'
)


COLLECTIVE_PRODB_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_PRODB_FIXTURE,),
    name='CollectiveProdbLayer:FunctionalTesting'
)


COLLECTIVE_PRODB_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_PRODB_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveProdbLayer:AcceptanceTesting'
)

# -*- coding: utf-8 -*-
# ++ This file `metaconfigure.py` is generated at 1/10/16 6:40 PM ++
import logging
import zope.interface
import zope.component.zcml
from Globals import DevelopmentMode
from zope.component import queryUtility
from .utils import SimpleLazyObject
from .utils import Local
from .interfaces import IProdDBConnection
from zope.configuration.exceptions import ConfigurationError
#import zope.configuration.xmlconfig.ParserInfo
from collective.proDB import _

__author__ = "Md Nazrul Islam<connect2nazrul@gmail.com>"

local_db_manager = Local()
CPDB_PREFIX = 'collective.proDB'
CPDB_CONFIG_ORDER_PARAM = 1
CPDB_CONFIG_ORDER_FILE = 2
CPDB_CONFIG_ORDER_CALLABLE = 3

logger = logging.getLogger(CPDB_PREFIX + '.metaconfigure')


@zope.interface.implementer(IProdDBConnection)
class ProDBConnection(object):
    """
    """
    def __init__(self, *args, **kwargs):
        pass


class ProDBConfiguration(object):

    """
    """

    def __init__(self, _context, name, atomic_requests=None, is_default=False):

        """
        :param _context:
        :param name:
        :param atomic_requests:
        :param is_default:
        :return:
        """
        self.__configure = dict()
        self.__configure['name'] = generate_id(name, context=_context)
        if is_default:
            local_db_manager['default'] = self.__configure.get('name')

        self.__configure['atomic_requests'] = atomic_requests

        zope.component.zcml.utility(
            _context,
            provides=IProdDBConnection,
            name=self.__configure.get('name'),
            component=SimpleLazyObject(self._connection_factory)
        )

        logger.info(_('collective.proDB: database configuration `%s` is registered' % name))

    def database(self, _context, **kwargs):
        """
        :param _context:
        :param kwargs:
        :return:
        """
        defaults = {
            'name': None,
            'host': None,
            'user': None,
            'password': None,
            'dbms': None,
            'port': None,
            'charset': None,
            'schema': None,
            'unix_socket': None,
            'create_user': None

        }
        for key in kwargs.keys():

            if key not in defaults.keys():
                raise TypeError(_("Invalid attribute `%s` for <prodb:database />" % key))

        # @TODO: validation goes here
        defaults.update(kwargs)
        logger.info(_("'collective.proDB: got database settings: %s" % kwargs))

        self.__configure['database'] = defaults

    def testing(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        defaults = {
            'name': None,
            'host': None,
            'password': None,
            'drop': None
        }
        for key in kwargs.keys():

            if key not in defaults.keys():
                raise TypeError(_("Invalid attribute `%s` for <dbpro:testing />" % key))
        # @TODO: validation goes here
        defaults.update(kwargs)

        self.__configure['testing'] = kwargs

    def advanced(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        defaults = {
            'config_order': None,
            'config_file': None,
            'config_callable': None,
            'before_database_creation': None,
            'after_database_creation': None,
            'before_database_drop': None,
        }
        for key in kwargs.keys():

            if key not in defaults.keys():
                raise TypeError(_("Invalid attribute `%s` for <dbpro:advanced />" % key))

        # @TODO: validation goes here
        defaults.update(kwargs)

        self.__configure['advanced'] = defaults

    def backup(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        defaults = {
            'enable': None,
            'archive': None,
            'archive_format': None,
            'storage': None,
            'api_key': None,
            'api_secret': None,

        }
        for key in kwargs.keys():

            if key not in defaults.keys():
                raise TypeError(_("Invalid attribute `%s` for <dbpro:backup />" % key))

        # @TODO: validation goes here
        defaults.update(kwargs)

        self.__configure['backup'] = defaults

    def replication(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        defaults = {
            'enable': None
        }
        for key in kwargs.keys():

            if key not in defaults.keys():
                raise TypeError(_("Invalid attribute `%s` for <dbpro:replication />" % key))

        # @TODO: validation goes here
        defaults.update(kwargs)

        self.__configure['replication'] = defaults

    def _connection_factory(self, **kwargs):
        """
        :return:
        """
        self._validate_configure()
        params = self._prepare_connection_params()
        return ProDBConnection(**params)

    def _validate_configure(self):

        return True

    def _prepare_connection_params(self):

        """
        :return:
        """
        return self.__configure

# Utilities Functions


def generate_id(name, context, duplicate_constraint=True, with_prefix=True):
        """
        :param name
        :param context
        :param duplicate_constraint
        :param with_prefix
        zope.configuration.xmlconfig.ParserInfo
        :return: string
        """
        _id = name
        if with_prefix:
            _id = "%s_%s" % (CPDB_PREFIX, _id)

        if duplicate_constraint:
            exist = queryUtility(IProdDBConnection, name=_id, context=context, default=None)
            if exist:
                raise ConfigurationError(_("Duplicate database configuration name. `%s` is already registered" % name))

        return _id

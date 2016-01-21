# -*- coding: utf-8 -*-
# ++ This file `adapters.py` is generated at 1/9/16 8:35 PM ++
import zope.interface
import zope.schema
from .vocabulary import ArchiveVocabulary, FileStorageVocabulary

from collective.proDB import _
__author__ = "Md Nazrul Islam<connect2nazrul@gmail.com>"


class IProDBConfiguration(zope.interface.Interface):

    """  """

    name = zope.schema.TextLine(
        title=_("Name of the configuration", default=u'Name of the configuration'),
        description=_('Name of this configuration/connector. Later on you can call according to name'),
        required=True
    )
    prefix = zope.schema.TextLine(
        title=_("Configuration prefix", default=u'Configuration prefix'),
        description=_('description', default=u'description'),
        required=False
    )
    autocommit = zope.configuration.fields.Bool(
        title=_("Auto commit", default=u'Auto commit'),
        description=_('description', default=u'description'),
        required=False,
        default=True
    )
    atomic_requests = zope.configuration.fields.Bool(
        title=_("Atomic requests", default=u'Atomic requests'),
        description=_('description', default=u'description'),
        required=False,
        default=True
    )
    is_default = zope.configuration.fields.Bool(
        title=_('Is this default configuration', default=u'Is this default configuration'),
        required=False
    )
    remove = zope.configuration.fields.Bool(
        title=_('Remove', default=u'Remove'),
        description=_('description', default=u'description'),
        required=False
    )


class IProDBDatabase(zope.interface.Interface):

    """  """
    name = zope.schema.TextLine(
        title=_("Database Name", default=u'Database Name'),
        description=_('description', default=u'description'),
        required=False,
    )
    host = zope.schema.TextLine(
        title=_("Database HOST", default=u'Database HOST'),
        description=_('description', default=u'description'),
        required=False,
    )
    user = zope.schema.TextLine(
        title=_("Database User", default=u'Database User'),
        description=_('description', default=u'description'),
        required=False,
    )
    password = zope.schema.TextLine(
        title=_("Database Password", default=u'Database Password'),
        description=_('description', default=u'description'),
        required=False,
    )
    dbms = zope.schema.TextLine(
        title=_("Database backend", default=u'Database backend')
    )
    port = zope.schema.Int(
        title=_("Database port", default=u'Database Password'),
        description=_('description', default=u'description'),
        required=False,
    )
    charset = zope.schema.TextLine(
        title=_("Default charset", default=u'Default charset'),
        description=_('description', default=u'description'),
        required=False,
        default=u'utf8'
    )
    schema = zope.configuration.fields.Path(
        title=_("Database schema", default=u'Database schema'),
        description=_('description', default=u'description'),
        required=False
    )
    unix_socket = zope.configuration.fields.Bool(
        title=_('Use UNIX Socket', default=u'Use UNIX Socket'),
        description=_('description', default=u'description'),
        required=False
    )
    create_user = zope.configuration.fields.Bool(
        title=_("Create user", default=u'Create user'),
        description=_('description', default=u'description'),
        required=False,
        default=False)


class IProDBDatabaseTesting(zope.interface.Interface):
    """
    """
    name = zope.schema.TextLine(
        title=_("Database HOST", default=u'Database HOST'),
        description=_('description', default=u'description'),
        required=False,
    )
    host = zope.schema.TextLine(
        title=_("Database HOST", default=u'Database HOST'),
        description=_('description', default=u'description'),
        required=False,
    )
    password = zope.schema.TextLine(
        title=_("Database Password", default=u'Database Password'),
        description=_('description', default=u'description'),
        required=False,
    )
    drop = zope.configuration.fields.Bool(
        title=_('Enable drop', default=u'Enable drop'),
        description=_('enable database drop after teardown', default=u'enable database drop after teardown'),
        required=False,
        default=True
    )


class IProDBDatabaseAdvanced(zope.interface.Interface):
    """
    """
    config_order = zope.configuration.fields.Tokens(
        title=_('configure order', default=u'configure order'),
        description=_('description', default=u'description'),
        required=False,
        value_type=zope.schema.Int()

    )

    config_file = zope.configuration.fields.Path(
        title=_('configure file', default=u'configure file'),
        description=_('description', default=u'description'),
        required=False
    )

    config_callable = zope.configuration.fields.GlobalObject(
        title=_('configure callable', default=u'configure callable'),
        description=_('description', default=u'description'),
        required=False
    )

    before_database_creation = zope.configuration.fields.GlobalObject(
        title=_('before database creation callable', default=u'before database creation callable'),
        description=_('description', default=u'description'),
        required=False
    )

    after_database_creation = zope.configuration.fields.GlobalObject(
        title=_('after database creation callable', default=u'after database creation callable'),
        description=_('description', default=u'description'),
        required=False
    )
    before_database_drop = zope.configuration.fields.GlobalObject(
        title=_('before database drop callable', default=u'before database drop callable'),
        description=_('description', default=u'description'),
        required=False
    )


class IProDBDatabaseBackup(zope.interface.Interface):

    """
    """
    enable = zope.configuration.fields.Bool(
        title=_('enable database backup', default=u'enable database backup'),
        description=_('description', default=u'description'),
        required=False
    )
    archive = zope.configuration.fields.Bool(
        title=_('enable archive', default=u'enable archive'),
        description=_('enable database dump file, transform to compressed archive format',
                      default=u'enable database dump file, transform to compressed archive format'),
        required=False
    )
    archive_format = zope.schema.Choice(
        title=_('archive format', default=u'archive format'),
        description=_('description', default=u'description'),
        required=False,
        vocabulary=ArchiveVocabulary
    )
    storage = zope.schema.Choice(
        title=_('storage type', default=u'storage type'),
        description=_('the location of backup file to be stored', default=u'the location of backup file to be stored'),
        required=False,
        vocabulary=FileStorageVocabulary
    )

    api_key = zope.schema.TextLine(
        title=_('api key', default=u'api key'),
        description=_('in case of remote location/cloud storage selected. for example dropbox or google drive.',
                      default=u'in case of remote location/cloud storage selected. for example dropbox or '
                              u'google drive.'),
        required=False
    )
    api_secret = zope.schema.TextLine(
        title=_('api secret', default=u'api secret'),
        description=_('same as api key', default=u'same as api key'),
        required=False
    )


class IProDBDatabaseReplication(zope.interface.Interface):
    """
    """
    enable = zope.configuration.fields.Bool(
        title=_('enable replication', default=u'enable replication'),
        description=_('description', default=u'description'),
        required=False
    )

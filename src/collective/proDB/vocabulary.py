# -*- coding: utf-8 -*-
# ++ This file `vocabulary.py` is generated at 1/12/16 6:26 PM ++
from zope.schema.vocabulary import SimpleVocabulary

__author__ = "Md Nazrul Islam<connect2nazrul@gmail.com>"

ArchiveVocabulary = SimpleVocabulary.fromItems((
        (u"ZIP", "zip"),
        (u"TAR", "tar"),
        (u"G ZIP", "gzip")
    ))

FileStorageVocabulary = SimpleVocabulary.fromItems((
    (u"local", "local"),
    (u"dropbox", "dropbox"),
    (u"Amazon Cloud", "aws"),
    (u"Google Drive", "google")
))

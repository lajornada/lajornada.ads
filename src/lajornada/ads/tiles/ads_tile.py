# -*- coding: utf-8 -*-
from zope.interface import implements

from zope import schema

from plone.tiles.interfaces import ITileDataManager

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile

from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from lajornada.ads.interfaces import AdsSettings

class IAds(IPersistentCoverTile):
   

    def delete():
        """
This method removes the persistent data created for this tile
"""

    def get_oas():
        """
Get the stored name.
"""

    def accepted_ct():
        """
Check wich content types are accepted.
"""


class Ads(PersistentCoverTile):

    index = ViewPageTemplateFile("templates/ads_tile.pt")
    implements(IPersistentCoverTile)
    is_configurable = False
    is_droppable = False
    is_editable = False
   
    def get_oas(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(AdsSettings)
        a1 = self.settings.adsBanner01
        a2 = self.settings.adsBanner02
        a3 = self.settings.adsBanner03
        a4 = self.settings.adsBanner04
       

    def delete(self):
        data_mgr = ITileDataManager(self)
        data_mgr.delete()

    def accepted_ct(self):
        return None

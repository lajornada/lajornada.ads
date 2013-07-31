from z3c.form import interfaces
from zope import schema
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('AdsControlPanel')


class AdsSettings(Interface):
    """Global Advertising settings. This describes records stored in
    configuration registry and obtainable via plone.registry.
    """
    adsBanner01 = schema.TextLine(title=_(u"location_01"),
                                  description=_(u"Code and location of ads space",
                                                default=u"oas code"),
                                  required=False,
                                  default=u'',)

    adsBanner02 = schema.TextLine(title=_(u"location_01"),
                                  description=_(u"Code and location of ads space",
                                                default=u"oas code"),
                                  required=False,
                                  default=u'',)

    adsBanner03 = schema.TextLine(title=_(u"location_01"),
                                  description=_(u"Code and location of ads space",
                                                default=u"oas code"),
                                  required=False,
                                  default=u'',)

    adsBanner04 = schema.TextLine(title=_(u"location_01"),
                                  description=_(u"Code and location of ads space",
                                                default=u"oas code"),
                                  required=False,
                                  default=u'',)

    adsBanner05 = schema.TextLine(title=_(u"location_01"),
                                  description=_(u"Code and location of ads space",
                                                default=u"oas code"),
                                  required=False,
                                  default=u'',)

    adsBanner06 = schema.TextLine(title=_(u"location_01"),
                                  description=_(u"Code and location of ads space",
                                                default=u"oas code"),
                                  required=False,
                                  default=u'',)

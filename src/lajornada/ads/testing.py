from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class LajornadaadsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import lajornada.ads
        xmlconfig.file(
            'configure.zcml',
            lajornada.ads,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'lajornada.ads:default')

LAJORNADA_ADS_FIXTURE = LajornadaadsLayer()
LAJORNADA_ADS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LAJORNADA_ADS_FIXTURE,),
    name="LajornadaadsLayer:Integration"
)
LAJORNADA_ADS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LAJORNADA_ADS_FIXTURE, z2.ZSERVER_FIXTURE),
    name="LajornadaadsLayer:Functional"
)

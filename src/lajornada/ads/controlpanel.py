from plone.app.registry.browser import controlpanel

from lajornada.portal.theme.interfaces import AdsSettings, _


class AdsSettingsEditForm(controlpanel.RegistryEditForm):

    schema = AdsSettings
    label = _(u"Ads settings")
    description = _(u"""""")

    def updateFields(self):
        super(AdsSettingsEditForm, self).updateFields()


    def updateWidgets(self):
        super(AdsSettingsEditForm, self).updateWidgets()

class AdsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = AdsSettingsEditForm



    <include package="plone.app.registry" />

    <!-- Control panel -->
    <browser:page
        name="ads-settings"
        for="Products.CMFPlone.interfaces.IPloneSiteRoot"
        class=".controlpanel.AdsSettingsControlPanel"
        permission="cmf.ManagePortal"
        />
    <genericsetup:registerProfile
      name="default"
      title="Ads settings control panel"
      directory="profiles/default"
      description="define ads spaces."
      provides="Products.GenericSetup.interfaces.EXTENSION"
      />

from  lajornada.ads.testing import LAJORNADA_ADS_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.txt"),
                layer=LAJORNADA_ADS_FUNCTIONAL_TESTING)
    ])
    return suite
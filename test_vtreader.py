# -*- coding: utf-8 -*-
#
# This code is licensed under the GPL 2.0 license.
#
import unittest
import os
import sys
from qgis.core import *
from qgis.utils import iface
from PyQt4.QtCore import *

from tile_source import MBTilesSource


class IfaceTests(unittest.TestCase):
    """
    Tests for Iface
    """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def testIfaceisNotNote(self):
        global iface
        self.assertIsNotNone(iface)


class MbtilesSourceTests(unittest.TestCase):
    """
    Tests for MBTilesSource
    """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def testMbtilesSourceCreation(self):
        path = os.path.join(os.path.dirname(__file__), 'sample_data', 'uster_zh.mbtiles')
        src = MBTilesSource(path)
        self.assertEqual(path, src.source())


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(IfaceTests))
    # suite = unittest.makeSuite(IfaceTests, 'test')
    return suite


# run all tests using unittest skipping nose or testplugin
def run_all():
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(suite())


if __name__ == "__main__":
    run_all()

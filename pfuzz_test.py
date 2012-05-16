#!/usr/bin/python

import unittest
import pf6mod_dhcp

class TestPF6modDHCP(unittest.TestCase):
    def setUp(self):
        self.seq = []
        for i in range(8):
            self.seq.append("1::%i" % i)

    def test_prefixprefix(self):
        for element in pf6mod_dhcp.plugin_main("1::"):
            self.assertTrue(element[0:3] == "1::")
            
    def test_usage(self):
        self.assertTrue (type(pf6mod_dhcp.plugin_usage()) is str)

    def test_desc(self):
        self.assertTrue (type(pf6mod_dhcp.plugin_description()) is str)
    
if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python

import unittest
import pf6mod_dhcp
import pf6mod_ports
import pf6mod_mac

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
        
class TestPF6modMAC(unittest.TestCase):
    def setUp(self):
        self.seq = []
        for i in range(8):
            self.seq.append("1::%i" % i)

    def test_get_orig_mac(self):
        self.assertTrue(type(pf6mod_mac.get_orig_mac("Xerox")) is list)
        self.assertEqual(pf6mod_mac.get_orig_mac("Xerox"), ['00:00:01', '00:00:02', '00:00:03', '00:00:04', '00:00:05', '00:00:06', '00:00:07', '00:00:08', '00:00:09', '00:00:AA', '9C:93:4E'])
            
    def test_usage(self):
        self.assertTrue (type(pf6mod_mac.plugin_usage()) is str)

    def test_desc(self):
        self.assertTrue (type(pf6mod_mac.plugin_description()) is str)
        
class TestPF6modPorts(unittest.TestCase):
    def setUp(self):
        self.seq = []
        for i in range(8):
            self.seq.append("1::%i" % i)

    def test_prefixprefix(self):
        for element in pf6mod_ports.plugin_main("1::"):
            self.assertTrue(type(element) is str)
            self.assertTrue(element[0:3] == "1::")
            check_int = int(element[element.rfind(":")+1:])
            self.assertTrue(type(check_int) is int)
            self.assertTrue(type(element[element.rfind(":"):]) is str)
            
    def test_usage(self):
        self.assertTrue (type(pf6mod_ports.plugin_usage()) is str)

    def test_desc(self):
        self.assertTrue (type(pf6mod_ports.plugin_description()) is str)
    
if __name__ == '__main__':
    unittest.main()
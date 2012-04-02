pfuzz
========

an IPv6 prefix fuzzer

requirements
--------------

python 2.6 or greater
python-netaddr


usage
------

$ pfuzz 2001:468:c80::

Create a list of addresses to scan that start with 2001:468:c80::

$ pfuzz 2001:468:c80:: --mac-org=Vmware

Specify the MAC originator to identify SLAAC hosts

$ pfuzz 2001:468:c80:: --mac-org=Xerox | nmap -iL - -F -6

Scan the hosts with nmap

$ pfuzz 2001:468:c80:[0-3]:1:[0-FF]:

Range queries

modules
--------
pfuzz has a modular design

ports - uses common ports to detect common service addresses
dhcp - scans common DHCP address ranges
mac - scan for devices based on SLAAC MAC


author
-------
Will Urbanski
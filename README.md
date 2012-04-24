pfuzz
========

pfuzz is an IPv6 prefix fuzzer. The massive amount of IPv6 address space makes it infeasable to scan for live hosts. This program permutates common and popular IPv6 addressing schemes. It can be used in conjucntion with a network scanner like nmap.

pfuzz has a modular design so it is easy to modify and improve.

usage
------

$ pfuzz 2001:468:c80::

Create a list of addresses to scan that start with 2001:468:c80::, using the default options (common DHCP addressing schemes)


$ pfuzz 2001:468:c80:: --mac-org=Vmware

Specify the MAC originator to identify SLAAC hosts


$ pfuzz 2001:468:c80:: --mac-org=Xerox | nmap -iL - -F -6

Scan any Xerox-related SLAAC hosts with nmap


$ pfuzz 2001:468:c80::[0-3]:F:[0-FF]

Range queries

modules
--------
ports - uses common ports to detect common service addresses
dhcp - scans common DHCP address ranges
mac - scan for devices based on SLAAC MAC

requirements
--------------

python 2.6 or greater
python-netaddr



author
-------
Will Urbanski
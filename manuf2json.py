#!/usr/bin/python

import re

manuf = open('manuf','r')
reMACLine = re.compile("[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}[ \t]+[A-Za-z0-9]+[ \t]+.*")

orgs = {}

for line in manuf.readlines():
    line = line.replace("\n","")
    match = reMACLine.search(line)
    if match and match != None:
        mac_prefix = line.split("\t")[0]
        mac_name = line.split("\t")[1].split(" ")[0]
        #print "%s - %s" % (mac_name, mac_prefix)
        try:
            orgs[mac_name].append(mac_prefix)
        except KeyError:
            orgs[mac_name] = []
            orgs[mac_name].append(mac_prefix)
        
print orgs['Vmware']
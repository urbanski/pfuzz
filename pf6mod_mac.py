#!/usr/bin/python

import re
import sys
import os
import  urllib2

MANUF_URL = "http://anonsvn.wireshark.org/wireshark/trunk/manuf"
MANUF_PATH = "/etc/manuf"

def get_orig_mac(mac_org):
    global MANUF_URL
    global MANUF_PATH
    
    if os.path.isfile(MANUF_PATH):
        manuf = open('manuf','r')
    else:
        manuf = urllib2.urlopen(MANUF_URL)
        
    #re to recognize manuf format
    reMACLine = re.compile("[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}[ \t]+[A-Za-z0-9]+[ \t]+.*")
    
    orgs = {}
    
    for line in manuf.readlines():
        line = line.replace("\n","")
        match = reMACLine.search(line)
        if match and match != None:
            mac_prefix = line.split("\t")[0]
            mac_name = line.split("\t")[1].split(" ")[0]
            try:
                orgs[mac_name].append(mac_prefix)
            except KeyError:
                orgs[mac_name] = []
                orgs[mac_name].append(mac_prefix)
                
    return orgs[mac_org]


def plugin_main(*args, **kwargs):
    prefix = args[0]
    app_args = args[1]
    addrs = []
    hexchars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    
    #check for mac origin company
    if (app_args.mac_org != None):
        hexprefixes = get_orig_mac(app_args.mac_org)
    else:
        hexprefixes = ["0000:00"]

    for hexprefix in hexprefixes:
        hextuple = []
        hexaddrs = []
    
        for c in hexchars:
            for d in hexchars:
                hextuple.append("%s%s" % (c,d))
        
        
        for x in hextuple:
            for y in hextuple:
                for z in hextuple:
                    hexaddrs.append("%s%s:%s%s" % (hexprefix,x,y,z))
    
    
        #print hexaddrs
        for hexaddr in hexaddrs:
            addrs.append("%s%s" % (prefix, hexaddr))
        
    return addrs
    
    
    

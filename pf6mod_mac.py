#!/usr/bin/python
#
#   pf6mod_mac
#
#   provides MAC (SLAAC) fuzzing for pfuzz
#
#   a project of the Dragon Research Group <dragonresearchgroup.org>
#   license: GNU GPL v3 <http://www.gnu.org/licenses/gpl-3.0.txt>
#   author: Will Urbanski <will.urbanski@gmail.com>
#

import re
import sys
import os
import urllib2

MANUF_URL = "http://anonsvn.wireshark.org/wireshark/trunk/manuf"    #the url to download manuf
MANUF_PATH = "/etc/manuf"                                           #the default manuf path if it's included with the system
MANUF_LOCAL = "pfuzz_manuf"                                         #the local copy of manuf that pfuzz will pull down

def download_manuf(url):
    try:
        manuf = urllib2.urlopen(url)
        return manuf
    except URLError:
        return None

#downloads the MAC hosts list
def get_orig_mac(mac_org):
    global MANUF_URL
    global MANUF_PATH
    global MANUF_LOCAL
    bLocalManuf = False
    
    if os.path.isfile(MANUF_PATH):
        manuf = open(MANUF_PATH,'r')
        bLocalManuf = True
    elif os.path.isfile(MANUF_LOCAL):
        manuf = open(MANUF_LOCAL, 'r')
        bLocalManuf = True
    else:
        manuf = download_manuf(MANUF_URL)
        if (manuf == None):
            return []
            
    #re to recognize manuf format
    reMACLine = re.compile("[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}[ \t]+[A-Za-z0-9]+[ \t]+.*")
    
    orgs = {}
    
    if (bLocalManuf == False):
        local_manuf_ptr = open(MANUF_LOCAL,'w')
    
    for line in manuf.readlines():
        if (bLocalManuf == False):
            local_manuf_ptr.write(line)
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
                
    if (bLocalManuf == False):
        local_manuf_ptr.close()
        
    return orgs[mac_org]

#describes how the plugin works
def plugin_description():
    return "Uses MAC addresses to identify SLAAC hosts"

#describes how to use the plugin
def plugin_usage():
    return "./pfuzz --mac-org=Vmware"

def plugin_main(*args, **kwargs):
    prefix = args[0]
    app_args = args[1]
    addrs = []
    hexchars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    
    #check for mac origin company
    if (app_args.mac_org != None):
        try:
            hexprefixes = get_orig_mac(app_args.mac_org)
        except KeyError:
            hexprefixes = []
            print "Fatal: MAC organization '%s' not found" % app_args.mac_org
            sys.exit(0)
    else:
        hexprefixes = ["0000:00"]

    for hexprefix in hexprefixes:
        hextuple = []
        hexaddrs = []
    
        for c in hexchars:
            for d in hexchars:
                hextuple.append("%s%s" % (c,d))
        
        xtuple = hextuple
        ytuple = hextuple
        ztuple = hextuple
        
        for x in xtuple:
            for y in ytuple:
                for z in ztuple:
                    hexaddrs.append("%sFF:FE%s:%s%s" % (hexprefix,x,y,z))
    
        #print hexaddrs
        for hexaddr in hexaddrs:
            addrs.append("%s%s" % (prefix, hexaddr))
        
    return addrs
    

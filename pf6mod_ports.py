#!/usr/bin/python

def plugin_description():
    return "Iterates common IPv6 and TCP port-related patterns"

def plugin_usage():
    return "./pfuzz --module=ports"

def plugin_main(*args, **kwargs):
    prefix = args[0]
    addrs = []
    ports = [21,22,23,25,80,135,139,443,445,666,999,3306,3389,4567]
    
    #iterate common ports
    for i in range(1,3):
        for p in ports:
            addrs.append("%s%i:%i" % (prefix, i, p))
            
    #some popular paths
    
    
    return addrs
    
    
    

#!/usr/bin/python

#
#   dhcp

def plugin_main(*args, **kwargs):
    prefix = args[0]
    addrs = []
    
    for i in range(1,100):
        addrs.append("%s%i" % (prefix, i))
    
    #Jagornet DHCP Server v1.1 
    #:2:1::/64
    for i in range(10,255):
        addrs.append("%s%s" % (prefix, hex(i)))
        
    #WIDE-DHCP
    for i in range(1000,2000):
        addrs.append("%s%s" % (prefix, i))
    
    
    return addrs
    
    
    #2:0A-2:FF
    
    

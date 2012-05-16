#!/usr/bin/python

#
#   dhcp

def plugin_usage():
    return "./pfuzz --module=dhcp"

def plugin_description():
    return "Iterates commonly used DHCP patterns"

def plugin_main(*args, **kwargs):
    prefix = args[0]
    addrs = []
    
    #the most common use case; ::1-100
    for i in range(1,100):
        addrs.append("%s%i" % (prefix, i))
    
    #Jagornet DHCP Server v1.1 
    #:2:1::/64
    for i in range(10,255):
        addrs.append("%s%s" % (prefix, hex(i)[2:]))
        
    #WIDE-DHCP
    for i in range(1000,2000):
        addrs.append("%s%s" % (prefix, i))
    
    
    return addrs
    
    
    #2:0A-2:FF
    
    

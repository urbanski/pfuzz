#!/usr/bin/python

#
#   dhcp
#   this checks for common dhcp patterns

def plugin_main(*args, **kwargs):
    prefix = args[0]
    addrs = []
    
    #return 1 - 1000
    for i in range(1,500):
        addrs.append("%s%i" % (prefix, i))
    
    for i in range(1000,2000):
        addrs.append("%s%i" % (prefix, i))
    
    return addrs
    
    
    

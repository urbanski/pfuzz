#!/usr/bin/python

#
#   dhcp
#   this checks for common dhcp patterns

def plugin_main(*args, **kwargs):
    prefix = args[0]
    addrs = []
    
    for i in range(1,1010):
        addrs.append("%s%i" % (prefix, i))
    
    return addrs
    
    
    

#!/usr/bin/python

def plugin_main(*args, **kwargs):
    prefix = args[0]
    addrs = []

    #A-F
    hexchars = ["A","B","C","D","E","F"]
    for hc in hexchars:
        addrs.append("%s%s" % prefix, hc)
        

    return addrs
    
    
    

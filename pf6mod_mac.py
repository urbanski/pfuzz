#!/usr/bin/python

def plugin_main(*args, **kwargs):
    prefix = args[0]
    addrs = []
    hexprefix = "0023:30"
    hexchars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

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
    
    
    

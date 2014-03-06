#!/usr/bin/python
__author__ = 'archmagece'

'''
Created on 2013. 1. 7.

@author: archmagece@gmail.com
'''

import cPickle
import os
#communicate with another process through named pipe
#one for receive command, the other for send command

def main():
    rfPath = "./p1"
    wfPath = "./p2"
    try:
        os.mkfifo(wfPath)
        os.mkfifo(rfPath)
#        os.get_fifo(wfPath)
#        os.get_fifo(rfPath)
    except OSError:
        pass
    rp = open(rfPath, 'r')
    response = rp.read()
    print "P2 hear %s" % response
    rp.close()
    wp = open(wfPath, 'w')
    wp.write("P2: I'm fine, thank you! And you?")        
    wp.close()
    rp = open(rfPath, 'r')
    response = rp.read()
    print "P2 hear %s" % response
    rp.close()

if __name__ == '__main__':
    main()
    pass
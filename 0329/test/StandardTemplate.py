#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Your Name'

import sys
def test():
    print type(sys.argv)
    args = sys.argv
    if   len(args) == 1:
        print "Hello World!"
    elif len(args) == 2:
        print "hello %s!" % args[1]
    else:
        print "Too many arguments!"

if __name__ == '__main__':
    print "Author is %s" % __author__
    test()
    

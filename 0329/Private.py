#!/usr/bin/env python
# -*- coding: utf-8 -*-

'private variable and function'

import sys

__author__ = 'Your Name'

def _private_1(name):
    return "Hello, %s" % name

def __private_2(name):
    return "Hi, %s" % name

def greeting(name):
    if   len(name) > 3:
        print _private_1(name)
    else:
        print __private_2(name)

if __name__ == '__main__':
    greeting(sys.argv[1]) 

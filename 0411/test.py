#!/usr/bin/env python
# -*-  coding: UTF-8 -*-

import os
from os import environ

print os
print environ

env = dict(environ)
print "after env"
print env

var = dict(a="1", b="2");
print var
print type(var)

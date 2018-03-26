#!/usr/bin/env python
# -*- coding: utf-8 -*-

classmates = []

classmates.append('Adam')
#print classmates[0]

classmates.insert(2, 'Shawn')
#print classmates[1]

#out of range
#classmates[2] = 'Mike'

print "print..."
print len(classmates)
print classmates[-1]

for x in classmates:
    print x

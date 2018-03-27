message = "Welcome to the year of 2018"
import re
p = re.compile('(\d+)')
m = p.search(message)

print m
print m.group(1)

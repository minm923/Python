scores = [100, 98, 88]

d = {'Mike':100, 'Jim':95, 'Shawn':scores}

print "..."

print d['Mike']
print d['Shawn']

d['Add'] = 99

d.pop('Jim')

d['Mike'] = 101

print "find start..."
res = 'Mike' in d
print res

res2 = d.get('Mike')
print res2

for x in d:
    print x


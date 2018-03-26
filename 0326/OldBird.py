# for
msg = "Hello" # Character List

for c in msg:
    print c

# Array Comprehensions
a = range(4)
b = [2*x for x in a if 0 == x%2]

print "Array a"
print a

print "Array b"
print b

# Function
def power(x):
    return x**2

d = power
print d(2)

d2 = lambda x : x**2
print d2(2)

# How to use lambda ?
def iter(func, list):
    return [func(x) for x in list if 0 == x%2]

l3 = iter(d2, range(4))
print "l3 ",l3

# print len range help(func name)


# check_call()
import subprocess;

check_call("ls -l .", shell=True);

age = 20

if age > 60:
    print "old people"
elif age > 30:
    print "mid people"
elif age > 18:
    print "young people"
else:
    print "kid"

classmates=('Amy', 'Mike')

for x in classmates:
    print x

nums = [1, 2, 3, 4, 5]

n = len(nums)
index = 0

while n >= 0:
    nums[index] = nums[index] * 2
    n = n - 1
    index = index + 1

for x in nums:
    print x

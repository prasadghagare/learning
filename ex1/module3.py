#tuples

#consider immutable list
t = (1,2,3,'me')

#t[2] = 5  -- not allowed

t = ([1,2,3], 4, 6)

#allowed following
t[0][2] = 4

#set
# internal DS hash
#Thus allows fast retrieval
s = set()

s.add(1)
s.add(2)
s.add(3)

print "is one in this set?", 1 in s
#also possible to construct set in following way
s1 = {1,2,3}

#ages = [23,41,73,37,81,12]


#dictionaries

d = {"prasad": 986, "jon":389}
print d.keys()

print d.items()

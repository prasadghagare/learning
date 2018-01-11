#variables:
"""variables are tags in Python.

Python is dynamically typed, which means that variables do not have a fixed type

They point or refer to objects.

"""
#Due to dynamic nature following is possible

my_name = 42

my_name = "Prasad"


#one can get current type of object a variable points to by following
print "type of my_name now", type(my_name)
#print ("now type is:", type(42))  ---  this is how PYTHON3 does printing


#Other datatypes:

#floats
pi_valaue = 3.14

#numbers!!!!!!

num1 = 42
num2 = 5

#gives quotient
print "num1/num2 = ", num1 / num2

#for precize value make at least 1 float
print "num1/num2 = ", 42.0/5

#standard remainder
print "remainder of 42/5 = ", 42 % 5

#why not quotient
print "why not quotient : ", 42 // 5

"""give me average of 34, 29 and 8"""
#displaying floats can be pain
#https://docs.python.org/2/tutorial/floatingpoint.html#tut-fp-issues

#booleans
i_am_good = True
i_am_better = False

#some more ways to print
print "am I feeling good ? %r" %i_am_good

print "I am %s and %d is my favorite number "%(my_name, 73)

#Advanced string formatting using format method
# https://docs.python.org/3/library/string.html#formatexamples



print """btw triple quotes are also treated like comments
they can span across lines
like this
"""

print " 'single quotes'"
print '"double!!"'

print r"escape \t with r"
print "\t cant escape \t"

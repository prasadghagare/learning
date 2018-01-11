#lets make a list

#they are really arrays
#https://docs.python.org/2/faq/design.html#how-are-lists-implemented

num = [23,41,73,37,81,12]

#check its type on your system

#access O(1)
print "index 2 = ", num[2]

#slice it
print "slicing operation again gives a list : ", num[3:6]

#print following line for me using string formatting and list access
#"Addition of second number 41 and last number 81 is 122 "

#skip an index
print "num only even indexed : ", num[::2]

#grow your list
num.append(64)

#append a list itself
num.append([1,2,3,"not just numbers"])

#pop the last element, it returns the removed item O(1)
print( num.pop())

#pop with index :
print(num.pop(0))
#make a stack datastructure for me
#remove the known element
num.remove(73)

#in test
print 81 in num
#To check complexity of these DS in Python : https://wiki.python.org/moin/TimeComplexity?


ages = [23,41,73,37,81,12]
print "sum ages earlier: ", sum(ages)

#for has meaning in Python for iterables
#list is an iterable
ages_5 = []
#Look at indentation : Python forces this
for age in ages:
    ages_5.append(age + 5)

print ages_5

#add alternate numbers of above list
i = 0
sum1 = 0
sum2 = 0
for age in ages_5:
    if i % 2 == 0:
        sum1 = sum1 + age
    else:
        sum2 = sum2 + age
    i+=1

sum1 = 0
sum2 = 0
for i , age in enumerate(ages_5):
    if i % 2 == 0:
        sum1 = sum1 + age
    else:
        sum2 = sum2 + age

print sum1

#can you make it shorter??
print sum(ages_5[::2])

#explain range and xrange

#list comprehensions
#creating lists from existing lists instead of using for
print [i + 6 for i in ages if i < 30 ]
#explain zip
#print squares of first 10 natural numbers using list comprehensions
#https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

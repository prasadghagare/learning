#functions

#they are objects as well

#use def to make them
#keyword argument conundrum
def send(message , recipient):
    """these are docstring: used
    for explaining the functions behaviour to client code
    show it by importing this module from shell
    function uses ppositional argument. compulsory in call
    """
    print "this message was sent from %s to %s: "%(message, recipient)

def send_cc(message, recipient, cc = "god"):
    """cc is keyword argument, not mandatory in function call
    as it uses the given default value if no value passed
    """
    print "this message was sent from %s to %s with %s in cc "%(message, recipient, cc)

#best way to call above function
#when you are passing a keyword argument, better use the keyword in call
#all positional arguments should be called first
send_cc("leonard","sheldon", cc = "raj")

#a function can be passed as argument to another function!!!!
def indirect(func, arg1, arg2):
        func(arg1, arg2)

indirect(send, "me", "you")


#generator functions

def gensquares(N):
        for i in range(N):
            yield i ** 2

for i in gensquares(5):
    print "square is : ", i

#why genearators

# Build and return a list
def firstn(n):
     num, nums = 0, []
     while num < n:
         nums.append(num)
         num += 1
     return nums

sum_of_first_n = sum(firstn(1000000))

#firstn function builds full list in the memory and then returns

def firstn_gen(n):
    num = 0
    while num < n:
    yield num
    num += 1

sum_of_first_n = sum(firstn(1000000))

#https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
"""

if __name__ == "__main__":
    send_cc("leonard","sheldon", cc = "raj")
"""

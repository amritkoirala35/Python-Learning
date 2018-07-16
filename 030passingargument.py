'''
Passing argument in the function 

'''

def add(a,b):
    sum = a+b
    return sum

result = add(12,5)
print(result)

print(add('Hello ,','Mr.Amrit Koirala!!'))


print('')

#Lets do Default Parameter

def default_param(a,b=5,c=10):
    return a+b+c

result = default_param(3)
print(result)
result1 = default_param(1,2,3)
print(result1)


import os
os.system('cls')  #To clear a print screen or make a new

#Nested function 

def f(a):
    def g(b):
        def h(c):
            return a*b*c
        return h 
    return g

print(f(12)(10)(2))



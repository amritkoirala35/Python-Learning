'''
Throwing an Exceptions 
'''

#Example 

'''
a = 'a'

def RaiseException(a):
    if type(a) != type('a'):
        raise ValueError ('This is not a string')

try : 
    RaiseException(a)

except ValueError  as e :
    print(e)

'''


#Another Example 


def TestCase (a , b):
    assert a<b , 'a is greater than b '
try :
    TestCase(3,2)
except AssertionError as e :
    print(e)



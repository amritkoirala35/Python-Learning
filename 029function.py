'''
Functions in Python 

Syntax is : 

def function_name ():
    code
    code 
    code

and can be call by function_name()
'''

def function():
    print('This is our first function!')


function()


#Another example 

def returning():
    return 'I am a result!'

result = returning()
print(result)


#Multiple value return 

def multival():
    return 'This is a result,',2

result=multival()
print(result)
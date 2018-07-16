'''
Lambda Function 

'''


f = lambda x , y : x + y

print(f(2,3))


#another Example // Nested lambda function  

f = lambda a : lambda b : lambda c : a*b*c

print(f(5)(3)(2))


#Another Example 

f = lambda c : lambda a,b: lambda d : (c*(a+b))%d

print(f(2)(4,3)(11))
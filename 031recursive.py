'''
Recursive funtion 

'''


def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n - 1)



x = int(input('Enter the value whose you want to know factorial :'))
ans = factorial(x)
print('')
print('Factorial of',x,'is: ',ans)



#Regular Recursion 

def sum(m):
    if m==1:
        return 1
    else:
        return m + sum(m-1)


#Tail Recursion 

def tail_sum(m,accumulator =0):
    if m ==0:
        return accumulator
    else:
        return tail_sum(m-1,accumulator+m)


print(sum(10))
print(tail_sum(10))
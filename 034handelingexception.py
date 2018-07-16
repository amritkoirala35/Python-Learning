'''
Actually Handeling Exception 

'''


try:
    a=5/0

except Exception as e :
    print(e)

# tells that what the error exactly on try 


try : 
    n = int ('AMRIT')

except Exception as e :
    print(e)


#Next Example 

try :
    m = int(input('Enter an Integer :'))

except ValueError:
    print('That is not an integer')



#Another Example 

try : 
    sum =0 
    file = open ('number.txt','r')
    for number in file :
        sum = sum + 1.0/int(number)
    print(sum)


except ZeroDivisionError:
    print('Number in file equal to zero!')

except IOError:
    print('File Does not exist')

finally : 
    print(sum)
    file.close()
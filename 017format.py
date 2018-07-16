#Format Methods Strings 


print('Today I had {0} cups of {1}'.format(3,'coffee'))
#here .format() inside of this format function changes that all on those curly brackets or format them according those format functions 

print('prices : ({0} , {1} , {2})'.format(2 , 500 ,300.25))  #No need , because of positional arguments 
print('prices : ({x} , {y} , {z})'.format(x= 2 , y= 500 ,z=300.25)) # Need of argument in format function because x , y , z are not representing postion like 0,1 2, 3 ...
print('The {vechile} had {0} crashes in {1} monthes'.format(5,6, vechile ='car'))
print('{:<20}'.format('text')) #Formating position from left and upto 
print('{:>20}'.format('text'))
print('{:b}'.format(10)) #Formating to binary , decimal to bimary convert
print('{:x}'.format(15)) #X for hexadecimal 
print('{:o}'.format(10)) # o for octal 
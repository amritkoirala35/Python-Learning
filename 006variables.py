#We talk here about variables 

#basicallly its a reserved memory location with some vlaues 


number = 2 
real = 2.2
word = "word"

#here number , real , word are variable and they are assigning with values 

print(word)       #it print the value assing to it 
print(type(word))   #it prints types the that variables i.e word which is string 
print(number+real)  #it adds two varaibl es with assigned values and prints sum as output 

a,b,c = 1, "Amrit Koirala" , 152207*73

print(c)
print(b)

#Lets see magic , you don;t need to define datatype its dynamic 

a =1 
b ="hari kumar"
a = b 

print(a)

#List of Keywords , don't name them as a variables 
import keyword 
print(keyword.kwlist)  #these gives the list of keywords thats you shouldn't be use a variable , makes confusing , cause they alreay  have meaning over here 


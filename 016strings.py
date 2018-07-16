#Strings 

string = 'I am a strings in Pyhton'


print(len(string)) #Gives length of string 

print(string[2])
print(string[10])  # 11th postion of string , (n-1)th position

print(string[-1])  # called reverse indexing and starts from -1 from back , here -1 givs 'n' 
print(string[-4])

print(string[5:11]) #print from 5th to 11th index of string 
print(string[:5])   #print upto 5th index i.e 6th character 
print(string[15:])  
print(string[ : ])


string1 = 'Con' + 'catenation'
print(string1)

string2 = 2*('Con' + 'catenation ')
print(string2)


#Replace the character in a string 

word = "Ford"
word = 'L' + word[1:]
print(word)


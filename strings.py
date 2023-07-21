string1 = 'my name is '
print(string1)

string2 = 'Nitish'
print(string2)

print(string1 + string2)

#access a character from a string
string3 = 'Nitish'
print(string3[2])
print(string3[0])

#reverse access
string4 = 'happy'
print(string4[-3])

#slicing
string5 = 'Morning'
print(string5[2:5])

# Python strings are immutable
string = 'Hello Friends'
string = 'Hello guys'
print(string)

#multiline strings
string = '''My name is Nitish and
currently, i am learning Python language '''
print(string)

#comparing strings
str1 = 'Mango'
str2 = 'Apple'
str3 = 'Mango'

print(str1 == str2)
print(str1 == str3)
print(str2 == str3)

#joining two strings
Intro = 'Nitish from '
Class = 'Btech cse'
result = Intro + Class
print(result)

#concatinating string
string = 'ERROR!'
print(string *2)

#iterating through a string
string = 'Python'
for letter in string:
  print(letter)

#length of string
string = 'Python'

#using in-check substring within a string
print('o' in 'Python')
print('g' in 'School')


print(len(string))

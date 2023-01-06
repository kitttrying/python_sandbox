# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Hary'
age = 12

# Concatenate - joining together two strings
# print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old')

# String Formatting

# Arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (Python 3.6+)
# print(f'Hello, my name is {name} and I am {age} years old')


# String Methods
s = 'helloworld'

# Capitalize string
print(s.capitalize()) # .title() ??? czym się różni

#Make all uppercase
print(s.upper())

#Make all lower
print(s.lower())

#Swap case
print(s.swapcase())

#Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

#Count
sub = 'h'
print(s.count(sub))

#Starts with
print(s.startswith('hello'))

#Ends with
print(s.endswith('d'))

#Split into a list
print(s.split())

#Find position
print(s.find('r')) # ignoruje spacje

#Is all alphanumeric
print(s.isalnum())

#Is alphabetic
print(s.isalpha())

#Is all numeric
print(s.isnumeric())



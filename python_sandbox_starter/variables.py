# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# x = 1 # int
# y = 2.5 # float
# name = 'Ada' #str
# is_cool = True # bool

# Multuple assigment
x, y, name, is_cool = (1, 2.5, 'Ada', True)
#print(x, y, name, is_cool)

# Basic math
a = x + y
# print(a)

# Casting
x = str(x) # string
y = int(y) # integer liczba całkowita
z = float(y) # liczba zmiennoprzecinkowa
# print(type(x))
# print(type(y), y) # wyżej jest int, dlatego y wyświetla się jako 2
# print(type(z), z) # y = 2.0, bo najpierw zostalo zmienione na int i z powrotem na float



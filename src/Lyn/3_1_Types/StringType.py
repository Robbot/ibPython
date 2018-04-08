'''
Created on 8 kwi 2018

@author: Roju
'''
x = 'test single quotes'

print('x is {}'.format(x))
print(type(x))

x = "test double quotes"
print('x is {}'.format(x))
print(type(x))

x = '''

test triple quotes what 
leads to 
multiline

'''
print('x is {}'.format(x))
print(type(x))
#strings are objects
x='seven'.capitalize()
print('x is {} but it is seven.capitalize'.format(x))
print(type(x))

x='seven'.upper()
print('x is {} but it is seven.upper'.format(x))
print(type(x))
#positional arguments {} can be more than one
x='seven {} {}'.format(8,9)
print('x is {} but it is seven.format with two positional arguments'.format(x))
print(type(x))
#swap positional arguments 0 and 1
x='seven {1} {0}'.format(8,9)
print('x is {} but it is seven.format with two swapped positional arguments'.format(x))
print(type(x))
#swap positional arguments 0 and 1 with nine zeros filled before or  after
x='seven {1:<09} {0:>09}'.format(8,9)
print('x is {} but it is seven.format with two swapped positional arguments and nine zeros before or after'.format(x))
print(type(x))
#swap positional arguments 0 and 1 with nine zeros or other numbers
x='seven {1:<09} {0:>09}'.format(8,9769876)
print('x is {} but there are nine zeros or other numbers before or after'.format(x))
print(type(x))
#fstring to get the same result of swap positional arguments 0 and 1 with nine zeros or other numbers
a=8
b=9
x=f'seven {a:<09} {b:>09}'
print('x is {} but there are nine zeros or other numbers before or after using fstring'.format(x))
print(type(x))



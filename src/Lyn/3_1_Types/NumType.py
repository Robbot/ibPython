'''
Created on 9 kwi 2018

@author: Roju
'''
#numeric formats are in type of int
x = 7
print('x is {}'.format(x))
print(type(x))
#numeric formats are in type of float
x = 7.0
print('x is {}'.format(x))
print(type(x))
#two integers divided gives you float (only in py3)
x = 7/3
print('x is 7/3 but it gives float equal {}'.format(x))
print(type(x))
#two integers module gives you int
x = 7//3
print('x is 7//3 but it gives module int equal {}'.format(x))
print(type(x))
#two integers float gives you int
x = 7%3
print('x is 7 % 3 but it gives reminder int equal {}'.format(x))
print(type(x))
#when you dealing with money, don't use float but import decimal
from decimal import *
a = Decimal ('.10')
b = Decimal ('.30')
x = a + a + a - b
print('x is 0.1+0.1+0.1-0.3 decimal type deals properly with money {}'.format(x))
print(type(x))

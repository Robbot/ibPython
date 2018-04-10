'''
Created on 10 kwi 2018

@author: Roju
'''
x = (1,2,3,4,5)
print('x is {}'.format(x))
print(type(x))
# but if you change values this is still tuple
x = (1,'two',3.0,[4,'four'],5)
print('x is {}'.format(x))
print(type(x))
print(type(x[1]))

# use id to learn that those tuples are different object but consists of the same element objects
x = (1,'two',3.0,[4,'four'],5)
y = (1,'two',3.0,[4,'four'],5)
print('x is {}'.format(x))
print('y is {}'.format(y))
print(id(x))
print(id(x[1])) 
print("this ^ object id")
print(id(y))
print(id(y[1])) 
print('and this ^ object id are equal')
# check is  this tuple
if isinstance (x,tuple):
    print('yep this is tuple')
if isinstance (y[3],list):
    print('yep y3 is list')
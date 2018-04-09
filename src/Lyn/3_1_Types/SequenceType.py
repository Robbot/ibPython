'''
Created on 9 kwi 2018

@author: Roju
'''
# sequence example which is mutable - you can assign value to position like this x[2]=345
x = [ 1, 2, 3, 4, 5 ]
for i in x:
    print('i is {}'.format(i))
print('assigned value to third element of sequence')
x[2] = 345
for i in x:
    print('i is {}'.format(i))
# tuple example which is immutable - you CAN'T assign value to position like this x[2]=345
print('below tuple - result the same but different element')
x = ( 1, 2, 3, 4, 5 )
for i in x:
    print('i is {}'.format(i))
# range example which is immutable - it starts from 0, but you set starting position and step like below
print('range example - result the same but different element')
x = range(1,6,1)
for i in x:
    print('i is {}'.format(i))
# dictionary example which is mutable - but it needs two elements on each row
print('dictionary example - result the same but different element')
x = {'one':1, 'two':2,'three':3,'four':4, 'five':5}
for i in x:
    print('i is {}'.format(i))
print('dictionary example print both elements')
for k, v in x.items():
    print('k is {} and v is {}'.format(k,v))
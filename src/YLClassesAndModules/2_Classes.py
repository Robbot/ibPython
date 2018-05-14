'''
Created on 14 May 2018

@author: Robert
'''
import random
from _ast import arg
faces = ('heads','tails')

def subproc():
    print('I do something')
    print('But return nothing')
    
subproc()
print(subproc())

def funcproc():
    return random.choice(faces)
for flipcoin in range(5):
    print(funcproc(), end=' ')
print()

def iadd(arg1, arg2):
    ''' Perform inline + operations'''
    return arg1 + arg2

print ('iadd(3,5) ->', iadd(3,5))
print('iadd("dy", "namic") ->', iadd ("dy", "namic")) 

def isum(*args):
    '''Return a total of the numeric args'''
    print('args ->', args)
    total = 0
    for arg in args:
        total += arg
    return total
print('isum(1,2,3,4,5) ->', isum(1,2,3,4,5))
#If you have already tuple you can pass this as parameter, just use *
params = (5,4,3,2,1)
print('isum(*params) ->', isum(*params))   

#kwargs keyword arguments

def iflex(**kwargs):
    print('kwargs ->', kwargs)
    for key in kwargs:
        print(key, '->', kwargs[key])
    return tuple(kwargs.values())

alphabet = {}

print ('iflex(**alphabet) ->', iflex(**alphabet))
alphabet = {'deleta':'δ', 'sigma':'σ','pi':'π'}
print ('iflex(**alphabet) ->', iflex(**alphabet))
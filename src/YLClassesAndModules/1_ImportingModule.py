'''
Created on 14 May 2018

@author: Robert
'''
import os

print(os.environ['PYTHONPATH'])

import sys
print(sys.path)

import random
sayings = ('Hello', 'Hi', 'Hey', 'Alo', 'Aloha')

def greet():
    return random.choice(sayings)
#it will return random greeting from sayings collection
print(greet())
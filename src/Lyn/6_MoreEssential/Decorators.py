'''
Created on 23 kwi 2018

@author: Roju
'''
def f1(f):
    def f2():
        print('this is before function call')
        f()
        print('this is after function call')
    return f2()
    
def f3():
    print('this is f3')
    
f3 = f1(f3)
f3
#  or you can use a decorator (@f7) which give you exactly same result like below:
def f7(f):
    def f8():
        print('this is before function call')
        f()
        print('this is after function call')
    return f8()
@f7 
def f9():
    print('this is f9')
    
f9
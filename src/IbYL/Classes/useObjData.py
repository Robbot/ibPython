'''
Created on 12 Apr 2018

@author: Robert
'''
class files:
    def __init__(self, ftype='text'):
        self._ftype='text'
    def move(self):
        print('file is moving')
    def copy(self):
        print('file is being copied')
    def delete(self):
        print('file is being removed')
    
    def set_ftype(self,ftype):
        self._ftype=ftype
        
    def get_ftype(self):
        return self._ftype
    
def main():
    execs=files()
    execs.move()
    execs.copy()
    # the below is getting from set method and from class
    print(execs.get_ftype())
    # now set to diffrent format
    execs.set_ftype('mov')
    print(execs.get_ftype())

main()
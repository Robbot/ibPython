'''
Created on 16 Apr 2018

@author: Robert
'''
class network:
    def cable(self): print('I am the cable')
    def router(self): print('I am the router')
    def switch(self): print('I am the switch')
    def wifi(self): print('I am wireless router, cable does not matter')

class tokenRing(network):
    def cable(self): print('I am a token ring cable')
    def router(self): print('I am a token ring router')
    
class ethernet(network):
    def cable(self): print('I am a ethernet cable')
    def router(self): print('I am a ethernet router')
    
def main():
    
    windows=tokenRing()
    mac=ethernet()
    #example of polimorphism - this is the same method cable but it takes data from different classes and gives different results
    windows.cable()
    mac.cable()
    # below it is even better implemented
    for obj in (windows, mac):
        obj.cable()
        obj.router()
        # obj.wifi is not definied in class windows or mac but it is taken from class network
        obj.wifi()
    
main()
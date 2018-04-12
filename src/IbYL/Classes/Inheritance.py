'''
Created on 12 Apr 2018

@author: Robert
'''
class fileSystem:
    def convertTo(self): print('I am converting to this filesystem')
    def dynamicPart(self): print('I am changing to a dynamic partition')
    def status(self): print('I am currently displaying the status of my system')
    def virtual(self): print('I am now a virtual file system')
    
class NTFS (fileSystem):
    def convertTo(self):
        #super is getting mehod from parent class
        super().convertTo()
        # but you can overwrite this too
        print('I have converted to NTFS filesystem')
        
def main():
    
    myFS=fileSystem()
    myFS.convertTo()
    
    myFS2=NTFS()
    myFS2.convertTo()
    # there is also available inherited methods
    myFS2.dynamicPart()
    myFS2.status()
    
main()
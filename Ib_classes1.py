class mailData:
    
    def sendMail(self): #define class method
        print("sending mail")
        
def main():
    mail = mailData() #create class instance
    mail.sendMail() #use class method
    
main() #run main method

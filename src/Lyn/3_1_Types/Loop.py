'''
Created on 11 kwi 2018

@author: Roju
'''
secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count +=1
    if count > max_attempt:  break
    if count == 3: continue
    pw = input(f"{count}: What's the secret word? ")
else:
    auth=True
    
print("Authorized" if auth else "Calling the FBI...")
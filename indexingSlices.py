def main():
    letters="abcdefghij"
    print("a letters string is "+letters)
    slice1=letters[1:3]
    print("print second and third letter from string what is "+slice1)
    slice2=letters[:3]
    print("print first three letters from string what is "+slice2)
    slice3=letters[1:] #it is not 0, but 1
    print("print everything except first letter from string what is "+slice3)
    slice4=letters[:-1] 
    print("print everything except the last letter from string what is "+slice4)
    
    # create a list of items
    items= ['bread','cheese','milk']
    print(items)
    slice5=items[1:3]
    print("print second and third item from items collection what is "+str(slice5))
    # now substitute milk for berries
    items[2]='berries'
    print(items)
    
    
main()
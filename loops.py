def main():

    data="this is where I want to break" #it breaks because of letter b in string
    for char in data:
        if char == 'b': break
        print(char, end='')
    else:
        print('else')
        
    
main()

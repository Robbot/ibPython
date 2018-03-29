from operator import itemgetter, attrgetter
def main():
    
    books = [('book1','w','6'),('book2','f','4'),('book3','c','7')]
    
    print(sorted(books,key=itemgetter(0)))
    print(sorted(books,key=itemgetter(1)))
    print(sorted(books,key=itemgetter(1), reverse=True))
    print(sorted(books,key=itemgetter(2)))
    
   # print(sorted(books,key=attrgetter('book'))) //because no attribute called book

if __name__ == '__main__':
    main()

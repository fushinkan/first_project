#This is the main file of the Library Management console app

from models import Book, BookWrapper

def main():
    
    author = 'Пушкин'
    title = 'Капитанская дочка'
    year = '1836'
    
    book = Book(author, title, year)
    dct = BookWrapper(book)
    print(book)
    print(dct.to_dict())
    
    
if __name__ == "__main__":
    main()
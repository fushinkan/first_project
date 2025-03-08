#This is the main file of the Library Management console app

from models import Book

def main():
    
    author = 'Пушкин'
    title = 'Капитанская дочка'
    year = '1836'
    
    book = Book(author, title, year)
    print(Book)
    
    
if __name__ == "__main__":
    main()
#This code wraps an instance of the Book class in a dictionary to write it to an instance of the Library class

from models import Book

class BookWrapper:
    
    def __init__(self, book: Book) -> None:
        self.book = book
        
    def to_dict(self) -> dict:
        return {
            'id': self.book.id,
            'author': self.book.author,
            'title': self.book.title,
            'year': self.book.year,
            'status': self.book.status
        }
        
    
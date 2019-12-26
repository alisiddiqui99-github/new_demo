class BookShelf:
    def __init__(self, *books):
        self.books = books


    def __str__(self):
        return f"<Book shelf contains {len(self.books)} Books>"

class Book:
    def __init__(self, name):
        self.name = name
        print(self.name)

    def __str__(self):
        return f"<Book {self.name}>"

book1 = Book('Harry Potter')
book2 = Book ("Letters from Khalil Gibran")
book3 = Book ("Python 101")

shelf = BookShelf(book1,book2 ,book3)
print(shelf)
print("He He He")

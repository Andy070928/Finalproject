class Book():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

class BookStore():

    def __init__(self):
        self.books = []
        self.filename = "books.txt"
        self.load()
    
    def load(self):
        try:
            with open(self.filename,'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts)==3:
                        title,author,price = parts 
                        self.books.append(Book(title,author,(price)))
        except FileNotFoundError:
                    pass
    def save(self):
        with open(self.filename,'w')as file:
            for book in self.books:
                file.write(str(book)+'\n')

    def add(self,book):
        self.books.append(book)
        print(f"Added book:{book.title}")

    def remove(self,title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed book:{book.title}")
                return
        print(f"Book with the title'{title}' not found.")

    def display(self):
        if not self.books:
            print("No books availble")
        else:
            for i,book in enumerate(self.books):
                print(f"{i +1}.{book.display()}")
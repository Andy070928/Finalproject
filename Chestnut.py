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
            
            

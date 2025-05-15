from Chestnut import Book, BookStore

def main():
    store = BookStore()

    while True:
        print("Welcome to the Bookstore")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. List all the book")
        print("4. Exist")
         
        choice = input("Enter your choice ")

        
        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            try: 
                price = float(input("Enter the book price: "))
                book = Book(title, author, price)
                store.add(book)
            except ValueError:
                print("Invalid price. Please enter a numeric value.")

        elif choice == '2':
            title = input("Enter the book title to remove: ")
            store.remove(title)

        elif choice == '3':
            store.display()

        elif choice == '4':
            store.save()
            print("Thank you for visiting the Book Store!")
            break

        else:
            print("Invalid choice. Please try again.")

main()
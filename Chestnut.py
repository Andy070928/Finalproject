            
class peach():
    def __init__(self):
        self.name="Andy"
        self.title="Moby Dick"



    def plus(self):
        self.title = input("what book would you like to add")

class peach():
    def __init__(self):
        self.author = ""
        self.title = ""        
        self.price = 0
        self.Books ={}
        self.people = ""       
    def plus(self):
        self.title = input("enter the name of the book you would like to plus:\n").upper
        self.author =input("enter the Author of the book you have just plused:\n").upper
        self.price =float(input("Enter the listing price of the book:\n"))

        self.Books [self.title] ={'Author':self.author,'Price':self.price}

        print("self.Books")


    def sell(self):
        self.people =input("enter the name of the books you want to sell:\n").upper
    try:
            str(peach.name)
            if peach.name in peach.Books:
                peach.Books.pop(peach.People)
                print("the remaining books are:",peach.Book)
    except:
        print("Please enter a book title")

    def showbook(self):
        for x in self.Books:
        #the Title, author, price




            print("\nBook title:",x,"")
          
            print(self.Books,{x}),{'author'}
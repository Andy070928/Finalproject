from Chestnut import peach

c = peach()

print(c.name)

v = input("Would you like to add a book('y'/'n')")
if v =="y":
    c = c.plus()
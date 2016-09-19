# Chris Gala 64338761 and Juan Reyes 71634415. ICS 31 Lab Sec 11. Lab asst 3.

### Part C1
##
##def abbreviate (n: str) -> str:
##    return n[0:3]
##assert abbreviate('January') == 'Jan'
##assert abbreviate('March') == 'Mar'
##assert abbreviate('June') == 'Jun'
##
##print(abbreviate("June"))
##
### Part C2
##print()
##
##def find_area_square (n: int) -> int:
##    return (n ** 2)
##assert find_area_square(2) == 4
##assert find_area_square(3) == 9
##assert find_area_square(4) == 16
##
##print(find_area_square(2))
##
###Part C3
##print()
##
##import math
##
##def find_area_circle (n: int) -> int:
##    return ((n**2)*math.pi)
##assert find_area_circle(2) == ((2**2)*math.pi)
##assert find_area_circle(3) == ((3**2)*math.pi)
##assert find_area_circle(4) == ((4**2)*math.pi)
##
##print(find_area_circle(2))

#Part C4
##print()
##
##def print_even_numbers (n: list):
##    for i in (n):
##        if (i % 2 == 0):
##            print(i)     
##print(print_even_numbers([2, 47, 31, 99, 20, 19, 23, 105, 710, 1004]))
##
###Part C5
##print()
##
##def calculate_shipping (n: int):
##    if (n < 2):
##        return(2.00)
##    if (2 <= n < 10):
##        return(5.00)
##    if (n >= 10):
##        return(5 + ((n-10)*1.50))
##assert calculate_shipping(1.5) == 2.00
##assert calculate_shipping(7) == 5.00
##assert calculate_shipping(15) == 12.50

#Part C6
##print()
##
##import tkinter
##
##def create_square (x: int, y: int, n: int):
##
##    my_window = tkinter.Tk()
##
##    my_canvas = tkinter.Canvas(my_window, width=500, height=500)
##    my_canvas.pack()
##
##    my_canvas.create_rectangle(x, y, x + n, y + n)
##    tkinter.mainloop()
##
##create_square(50, 50, 100)
##create_square(25, 25, 50)
##create_square(75, 75, 150)

#Part C7
##print()
##
##import tkinter
##
##def create_circle (x: int, y: int, n: int):
##    my_window = tkinter.Tk()
##
##    my_canvas = tkinter.Canvas(my_window, width=500, height=500)
##    my_canvas.pack()
##
##    my_canvas.create_oval(x, y, x + n, y + n)
##    tkinter.mainloop()
##
##create_circle(70, 70, 150)

#Part D.1
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')

RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50) ]

'''def restaurant_price (RC):
    return RC.price
assert restaurant_price(RC[0]) == 12.50
print(restaurant_price(RC[1]))'''
##
###Part D.2
##RC.sort(key=restaurant_price)
##print(RC)

#Part D.3
##RC.sort(key=restaurant_price)
##def costliest (RC):
##    return RC.name
##print(costliest(RC[-1]))

#Part D.4
##print(RC)
##RC.sort(key=restaurant_price)
##def costliest (RC):
##    return RC.name
##print(costliest(RC[-1]))
##print(RC)

##sorted(RC, key=restaurant_price)
##def costliest2 (RC):
##    return RC.name
##print(costliest2(RC[-1]))

#Part E.1
Book = namedtuple('Book', 'author title genre year price instock')

BSI = [
        Book("J.K. Rowling", "Harry Potter A", "Fantasy", "2000", 5.00, 5), 
        Book("J.K. Rowling", "Harry Potter B", "Fantasy", "2001", 5.00, 6), 
        Book("J.K. Rowling", "Harry Potter C", "Fantasy", "2002", 5.00, 7), 
        Book("J.K. Rowling", "Harry Potter D", "Fantasy", "2003", 5.00, 8), 
        Book("J.K. Rowling", "Harry Potter F", "Fantasy", "2004", 5.00, 9), 
        Book("J.K. Rowling", "Harry Potter E", "Fantasy", "2005", 5.00, 10) ]

##for i in range(len(BSI)):
##    print (BSI[i].title)

#Part E.2
def book_name2 (BSI: Book) -> str:
    return BSI.title
Booklist = sorted(BSI, key=book_name2)

for i in range(len(Booklist)):
    print (Booklist[i].title)

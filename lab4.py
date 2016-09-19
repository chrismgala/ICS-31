# Diana Dieu 51895226 and Chris Gala 64338761. ICS 31 Lab sec 11. Lab asst 4.
#jnthnyn@gmail.com
#
#
# Part (c)
#
#

# PART C1
print('---------------------Part C1-----------------------')
def test_number (n: int, s: str) -> bool:
    '''Takes a number and a string and evaluates whether the number is positive,
    negative, even, or odd based on the string input'''
    if s == 'even':
        if n%2==0:
            return True
        else:
            return False
    if s == 'odd':
        if n%2 !=0:
            return True
        else:
            return False
    if s == 'positive':
        if n > 0:
            return True
        else:
            return False
    if s == 'negative':
        if n < 0:
            return True
        else:
            return False
assert test_number(14, 'even')
assert not test_number (100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')

print(test_number(12, 'even'))
print(test_number(-89, 'positive'))

# PART C2
print('---------------------Part C2-----------------------')
def display():
    '''Takes a string and prints out each character of the string, line by line'''
    string = str(input('Enter the word:'))
    for i in range(len(string)):
        print(string[i])

display()

# PART C3
print('---------------------Part C3-----------------------')
def square_list (L:list) -> int:
    '''Takes a list of integers and prints each integer squared'''
    for i in range(len(L)):
        print(L[i]**2)
        
square_list([3,5,7,12,8])


# Part C4
print('---------------------Part C4-----------------------')
def match_first_letter(s: str, k:list) -> str:
    '''Takes a one character string and a list of strings and matches the one character to the first letter of the strings in the
second list and prints only the matches from the second list'''
    for i in range(len(k)):
        if s == k[i][0]:
            print(k[i])
match_first_letter('J', ['Jack', 'Jill', 'John', 'George'])

# Part C5
print('---------------------Part C5-----------------------')
def match_area_code (a:list, b:list) -> str:
    '''Takes a list of area codes and a list of phone numbers and prints the phone numbers that have the
area codes from the first list'''
    for i in range(len(b)):
        if b[i][1:4] in a:
            print(b[i])
match_area_code(['949', '714'], ['(949)556-7777', '(626)777-9090', '(714)555-2324', '(323)553-2312'])


# Part C6
print('---------------------Part C6-----------------------')
def match_area_codes (a:list, b:list) -> str:
    '''Takes a list of area codes and a list of phone numbers and returns the area codes that
match the phone numbers in the second list'''
    for i in range(len(b)):
        if b[i][1:4] in a:
            print(b[i][1:4])
match_area_codes(['949', '714'], ['(949)556-7777', '(626)777-9090', '(714)555-2324', '(323)553-2312'])

#
#
# Part (d)
#
#

# Part D1
print('---------------------Part D1-----------------------')
vowel = ('aeiou')
def is_vowel(a: str) -> bool:
    '''Takes one character long strings and returns whether True or False if that character is a vowel'''
    return a in vowel
print(is_vowel('b'))

#Part D2
print('---------------------Part D2-----------------------')
def print_nonvowels(a: str) -> str:
    '''Takes a string and prints out all of the characters in the string that are not vowels'''
    for i in a:
        if is_vowel(i) == False:
            print(i)
print_nonvowels('bug')

#Part D3
print('---------------------Part D3-----------------------')
def nonvowels(a: str) -> str:
    '''Takes a string and returns a string containing the nonvowels from the first string'''
    result = ''
    for i in a:
        if is_vowel(i) == False:
            result += i
    return result
print(nonvowels('bad.'))
print(nonvowels('.!'))

#Part D4
print('---------------------Part D4-----------------------')
consonants_list = ('bcdfghjklmnpqrstvxyz')
def consonants (a: str) -> str:
    '''Takes a string and returns a string containing only consonants from the input string'''
    result2 = ''
    for i in a:
        if i in consonants_list:
           result2 += i
    return result2
print(consonants('bad.'))

#Part D5
print('---------------------Part D5-----------------------')
def select_letters(a: str, b: str) -> str:
    '''Takes an input character and depending on the input, returns a string containing vowels or
consonants from the second input'''
    result3 = ''
    if a == 'v':
        for i in b:
            if is_vowel(i) == True:
                result3 += i
        return result3
    elif a == 'c':
        for i in b:
            if i in consonants_list:
                result3 += i
        return result3
    else:
        return result3
print(select_letters('v', 'bad'))
print(select_letters('c', 'bad'))
print(select_letters('d', 'bad'))

#Part D6
print('---------------------Part D6-----------------------')
def hide_vowels(a: str) -> str:
    '''Takes input string, then returns the same string with hyphens in place of the vowels'''
    hidden_vowels = ''
    for i in a:
        if i in vowel:
            hidden_vowels = a.replace(i, '-')
            print(hidden_vowels)
hide_vowels('Chris')

#Part E
print('---------------------Part E-----------------------')
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')

def Restaurant_change_price(r: Restaurant, n: int) -> Restaurant:
    '''Takes a namedtuple and a number and subtracts the number from the namedtuple (Restaurant's) price field'''
    return Restaurant(r.name, r.cuisine, r.phone, r.dish, r.price - n)
print(Restaurant_change_price(Restaurant('C', 'Indian', 123, 'Paneer', 3), 1))

#Part F1
print('---------------------Part F1-----------------------')
R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 

RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]

#Part F1
print('---------------------Part F1-----------------------')
def alphabetical(r: list) -> list:
    '''Takes a list and sorts it into alphabetical order by name and returns that into a list'''
    r.sort()
    return r
print(alphabetical(RL))

#Part F2
print('---------------------Part F2-----------------------')
def alphabetical_names(r: list) -> list:
    '''Takes a list and prints the names only in alphabetical order'''
    for i in range(len(r)):
        print(r[i][0])
alphabetical_names(RL)

#Part F3
print('---------------------Part F3-----------------------')
def all_Thai(r: list) -> list:
    '''Takes a list and rturns only the Thai restaurants' information in that list'''
    for i in range(len(r)):
        if r[i].cuisine == "Thai":
            print(r[i])
all_Thai(RL)

#Part F4
print('---------------------Part F4-----------------------')
def select_cuisine(r: list, s: str) -> list:
    '''Takes a list and a user selected cuisine and returns only the restaurants of that cuisine in a list'''
    for i in range(len(r)):
        if s == r[i].cuisine:
            print(r[i])
select_cuisine(RL, 'Thai')

#Part F5
print('---------------------Part F5-----------------------')
def select_cheaper(r: list, n: float) -> list:
    '''Takes a list and a number and returns only the restaurants with prices lower than the input number'''
    for i in range(len(r)):
        if r[i].price < n:
            print(r[i])
select_cheaper(RL, 6)

#Part F6
print('---------------------Part F6-----------------------')
def average_price(r: list) -> float:
    '''Takes a list and returns the average price of the restaurant prices in that list'''
    price_total = 0
    price_average = 0
    for i in range(len(r)):
        price_total = price_total + r[i].price
    price_average = price_total / len(r)
    return price_average
print(average_price(RL))

#Part F7
print('---------------------Part F7-----------------------')

#Part F8
print('---------------------Part F8-----------------------')

#Part F9
print('---------------------Part F9-----------------------')
print(select_cheaper(RL, 15))

#Part G
print('---------------------Part F9-----------------------')
import tkinter
my_window = tkinter.Tk()

my_canvas = tkinter.Canvas(my_window, width=500, height=500)
my_canvas.pack()

def create_rectangle_from_center(x: int, y: int, h: int, w: int):
    my_canvas.create_rectangle(x, y, h, w)
create_rectangle_from_center(50, 50, 100, 75)
tkinter.mainloop()

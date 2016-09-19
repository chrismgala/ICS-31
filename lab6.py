#Chris Gala 64338761 and Eui Seon Chi 83682606.  ICS 31 Lab 6 Sec 11, Lab asst 6

#C1
print('-------------------C1------------------------')
def contains(string: str, string2: str) -> bool:
    return string2 in string
assert contains('banana', 'ana') == True
assert not contains('racecar', 'ck') == True

#C2
print('-------------------C2------------------------')
def sentence_stats(string: str):
    nonpunctuation = str.maketrans('.,!?;:"',
                       '       ')
    num = 0

    string.translate(nonpunctuation)
    print("Characters: " + str((len(string))))
    print("Words: " + str(len(string.split())))

    for i in range(len((string.split()))):
        num += len(string.split()[i])
                   
    print("Average length: " + str(num/len(string.split())))

sentence_stats('I love UCI')

#C3
print('-------------------C3------------------------')
def initials(string: str):
    initials = ''
    for i in range(len(string.split())):
        initials += string.split()[i][0].upper()
    return initials
assert initials('Bill Cosby') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'

#D1
print('-------------------D1------------------------')
from random import randrange
for i in range(50):
    print(randrange(1, 7))

#D2
print('-------------------D2------------------------')
print()
def roll2dice() -> int:
    num = 0
    num2 = 0
    num += randrange(1, 7)
    num2 += randrange(1, 7)
    return num + num2
print(roll2dice())

for i in range(50):
    print(roll2dice())

#D3
print('-------------------D3------------------------')
def distribution_of_rolls(number:int):
    num = 0
    num2 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    num7 = 0
    num8 = 0
    num9 = 0
    num10 = 0
    num11 = 0
    num12 = 0
    num13 = 0
    num14 = 0
    for i in range(number):
        num = 0
        num2 = 0
        num += randrange(1, 7)
        num2 += randrange(1, 7)
        num3 = num + num2
        if num3 == 2:
            num4 += 1
        if num3 == 3:
            num5 += 1
        if num3 == 4:
            num6 += 1
        if num3 == 5:
            num7 += 1
        if num3 == 6:
            num8 += 1
        if num3 == 7:
            num9 += 1
        if num3 == 8:
            num10 += 1
        if num3 == 9:
            num11 += 1
        if num3 == 10:
            num12 += 1
        if num3 == 11:
            num13 += 1
        if num3 == 12:
            num14 += 1
    print("2: ", (num4), "(", ((num4/number)*100), "%)")
    print("3: ", (num5), "(", ((num5/number)*100), "%)")
    print("4: ", (num6), "(", ((num6/number)*100), "%)")
    print("5: ", (num7), "(", ((num7/number)*100), "%)")
    print("6: ", (num8), "(", ((num8/number)*100), "%)")
    print("7: ", (num9), "(", ((num9/number)*100), "%)")
    print("8: ", (num10), "(", ((num10/number)*100), "%)")
    print("9: ", (num11), "(", ((num11/number)*100), "%)")
    print("10: ", (num12), "(", ((num12/number)*100), "%)")
    print("11: ", (num13), "(", ((num13/number)*100), "%)")
    print("12: ", (num14), "(", ((num14/number)*100), "%)")
    print((number),"rolls")
    
distribution_of_rolls(20)

#E
print('-------------------E1------------------------')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#E1
#def Caesar_encrypt(string: str, key: int) -> str:

def rotated_alphabet(num: int):
    rotated = str.maketrans(alphabet, alphabet[num:]+alphabet[:num])
    return

print(rotated_alphabet(1))

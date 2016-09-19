def new_screen(rows: int, columns: int) -> 'list of lists, 2D table':
    ''' Return a list of rows, each row containing pixels going across.
        Whole screen starts out 0 (black).
    '''
    result = [ ]
    for r in range(rows):
        result.append([0]*columns)
    return result
s1 = new_screen(5, 10)
print(s1)

def print_screen(s: 'list of lists, 2D table') -> None:
    ''' Print screen in matrix form with * for black, blank for white
    '''
    for row in range(len(s)):
        for col in range(len(s[0])):
            if s[row][col] == 1:
                pixel = ' '
            else:
                pixel = '*'
            print(pixel, sep="", end="")
        print()  # End of row, print a newline
    return
print_screen(s1)

print('ABC', 'G', end="")
print()
 
D = {'Huey': 17, 'Dewey': 23, 'Louie': 42}
print(D)
print(D['Dewey'])

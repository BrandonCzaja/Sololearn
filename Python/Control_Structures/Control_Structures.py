# If statement Syntax: Don't forget the colon
# if expression:
#     statements

# Example
# if 10 > 5:
#     print("10 is greater than 5")

# print('Program ended')


# Example
# spam = 7
# if spam > 5:
#     print('five')
# if spam > 8:
#     print('eight')


# Nesting If Statements
num = 12
if num > 5:
    print('Bigger than 5')
    if num < 47:
        print('Between 5 and 47')

num = 7
if num > 3:
    print('3')
    if num < 5:
        print('5')
        if num == 7:
            print("7")
# This results in the output of 3 because once num is checked against 5 it exits the program


# IF ELSE STATEMENTS
x = 4
if x == 5:
    print('Yes')
else:
    print('No')

# Example:
if 1 + 1 == 2:
    if 2 * 2 == 8:
        print("if")
    else:
        print("else")

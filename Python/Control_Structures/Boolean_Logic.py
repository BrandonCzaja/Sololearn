# Boolean logic operators are (and, or, not)

# And Operator
# print(1 == 1 and 2 == 2)
# print(1 == 1 and 2 == 3)
# print(1 != 1 and 2 == 2)
# print(2 < 1 and 3 > 6)


# Example of boolean logic with an if statement
# I can either leave the expressions unwrapped, wrap each individual statement or wrap the whole if condition in ()
if (1 == 1 and 2 + 2 > 3):
    print('true')
else:
    print('false')


# Or Operator
age = 15
money = 500
if age > 18 or money > 100:
    print('Welcome')


# Not Operator
# print(not 1 == 1)  # False
# print(not 1 > 7)  # True

if not True:
    print('1')
elif not (1 + 1 == 3):
    print("2")
else:
    print("3")

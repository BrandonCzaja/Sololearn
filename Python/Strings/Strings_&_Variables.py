print('Python is fun!')
print('Always look on the bright side')


# Escaping characters
print("And then he said \"Hi everybody!\" and we all laughed")


# Newlines: \n
print('Line One \nLine Two, \nLine Three')

print("""this is
a multiline 
text""")  # Three quotes automatically creates a multiline quote where you indicate it to

# Concatenation
print("Green" + " " + "Eggs" + " " + "and " + "Ham")


# Multiplying Strings: Must add space or its all one big word
print('Spam ' * 3)
print(4 * 'Honey ')

# Variables
# Don't need let const or var
# Only letters numbers and underscores can be used, can't start with numbers
player = "Brandon"
player = 1
# Variables don't have types so you can change them
print(player)


# User input
text = input('Enter your name: ')
print(text)

age = int(input('Enter you age: '))
ageStr = age
print('His age is ' + str(age))

name = input('Random name: ')
lastName = input('Random last name: ')
print(name + lastName)

# Example
x = int(input('Value for x: '))
y = int(input('Value for y: '))
print(x + y)

# Lists are the python equivalent to js arrays

nums = [5, 4, 3, 2, 1]
print(nums[1])

# Empty List
empty_list = []
print(empty_list)

# Storing multiple data types in a single list
number = 3
things = ['string', 0, [1, 2, number], 4.56]


# Nesting Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # prints 6


# Strings also can be index like lists
str = "Hello world!"
print(str[5])  # Prints the blank space
print(str[6])


# List Operations
nums = [7, 7, 7, 7, 7, 7, 7]
nums[2] = 5
print(nums)
print(nums + [4, 5, 6])
# Increases the list size by 3x but does not increase the indexes' values
print(nums * 3)


# In Operator
# Checks if an item is in the list
words = ["spam", 'eggs', 'green', 'sausage']
print("spam" in words)  # Prints True
print('eggs' in words)  # Prints True
print('tomato' in words)  # Prints False

# Not Operator is the opposite of the In Operator
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

if "spam" in words:
    print('Yes')
    if 2 in nums:
        print("Also Yes")

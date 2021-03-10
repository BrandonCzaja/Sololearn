# The range function returns a sequence of numbers. By default it starts from 0 and increments by 1 and stops before the specified number
numbers = (list(range(10)))
# print(numbers)

more_numbers = list(range(20, 40))
# print(more_numbers)

my_object = range(20)
print(my_object)

for num in my_object:
    print(num)
# print(range(20) == range(0, 20))


# Step argument
numbers = list(range(0, 11, 2))
reverse_numbers = list(range(10, -1, -2))
print(reverse_numbers)
print(numbers)

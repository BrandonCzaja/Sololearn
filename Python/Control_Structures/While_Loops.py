i = 1
while i <= 5:
    print(i)
    i = i + 1

print('done')


j = 3
while j >= 0:
    print(j)
    j = j - 1
print('complete')


x = 1
while x < 10:
    if (x % 2 == 0):
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1
print("complete")


# Use Break Statements to end the loop prematurely
a = 0
while True:
    print(a)
    a += 1
    if a > 5:
        print('Breaking')
        break
print("Finish")


# Continue Statement
# A Continue Statement jumps back to the top of the loop rather than stopping it. It stops the current iteration and continues with the next one
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        print('Skipping 3')
        continue

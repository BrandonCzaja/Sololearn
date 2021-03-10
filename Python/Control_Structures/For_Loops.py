words = ['hello', 'greetings', 'welcome']
for cheese in words:
    print(cheese + "!")


str = 'practicing for loops'
count = 0
iteration = 0
for char in str:
    print(iteration)
    iteration += 1
    if iteration == 5:
        print('Continue')
        continue

    if iteration > 10:
        break

    if char == 't':
        count += 1

print(count)
print(iteration)

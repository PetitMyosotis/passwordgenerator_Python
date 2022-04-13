import random
import string
letters = list(string.printable)
print("Enter the password lenght")
passwordLenght = int(input())
random.shuffle(letters)
myList = []
for i in range(passwordLenght):
    myList.append(random.choice(letters))

iteration = 0
for i in range(passwordLenght):
    print(myList[iteration], end="")
    iteration = iteration + 1


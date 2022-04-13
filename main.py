import random
import string
# all the printable in a variable
letters = list(string.printable)
#message for the user
print("Enter the password lenght")
# get the user input
passwordLenght = int(input())
# mix the printable
random.shuffle(letters)
# create a empty list
myList = []
#put a random letters in the list
for i in range(passwordLenght):
    myList.append(random.choice(letters))
# variable to get the iteration
iteration = 0
# loop to print every letter/printable
for i in range(passwordLenght):
    print(myList[iteration], end="")
    iteration = iteration + 1


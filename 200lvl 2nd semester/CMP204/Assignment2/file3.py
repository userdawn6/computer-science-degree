import os

i = "Y"
while "Y":
	fileHand = open("names3 .txt", "a")
	class_size = int(input("How many students do you want to register?: ")) # introduce a class size variable to get the number of registering students instead of hard-coding it
	for names in range(0,class_size):
		name = input(str("What is your name?: "))
		fileHand.write(name + '\n')

	i = input(str("Do you want to continue?Y/N: "))
	if i == "N":
		break
fileHand.close()

# The code works as expected but still exhibits the behaviour from file 2 where the entries are on one line.


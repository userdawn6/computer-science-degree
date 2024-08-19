

fileHand = open("names2.txt", "a")

class_size = int(input("How many students do you want to register?: ")) 
for names in range(0,class_size):
	name = input(str("What is your name?: "))

	fileHand.write(name + '\n')

fileHand.close()



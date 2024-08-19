import os

fileHand = open("names1.txt", "a")

name = input(str("What is your name?: "))

fileHand.write(name)
fileHand.close()


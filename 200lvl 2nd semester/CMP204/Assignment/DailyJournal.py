import datetime

now = datetime.datetime.now()
i = "Y"
while "Y":
	file = open("journal_logs.txt", "a")
	log = input("What would you like to document today?: ")
	file.write(log + " " + "(Entry timestamp: " + " " + now.strftime("%Y-%m-%d %H:%M:%S") + ")" + "\n" + "="*50 + "\n")

	i = input("Do you want to add another entry? Y/N: ").upper()
	if i == "N":
		break

file.close()

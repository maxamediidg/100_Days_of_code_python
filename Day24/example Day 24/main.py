with open("My_file.txt") as file:
	contents = file.read()
	print(contents)

with open("new_file.txt", mode="w") as file:
	file.write("\nNew text.")


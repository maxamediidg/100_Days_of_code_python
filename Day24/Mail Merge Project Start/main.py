PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt") as names_files:
	names=names_files.readlines()
	print(names)

with open("./input/Letters/starting_letter.txt") as letter_file:
	letter_Contents = letter_file.read()
	for name in names:
		strip_name =name.strip()
		new_letter =letter_Contents.replace(PLACEHOLDER, strip_name)
		with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as completed_letter:
			completed_letter.write(new_letter)



def getinput(prompt=None):
	if prompt != None:
		inputed = input(prompt + " ")
	else:
		inputed = input()
	stringed = str(inputed)
	choice = str.upper(stringed)
	return choice

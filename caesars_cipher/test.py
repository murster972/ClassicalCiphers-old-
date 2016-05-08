word = "CAOSSLRNLIRLPEMSOA EUCEYPBFLOSOMVWIU"
numericList = []
x = 0

for c in word:
	numericList.append(ord(c))

while x < 26:
	key = x
	cipherList = ""

	for i in numericList:
		if chr(i + key) > chr(90):
			NEW_KEY = (i + key) - 26
			cipherList += chr(NEW_KEY)
					

		elif i != 32:
			cipherList += chr(i + key)

		elif i == 32:
			cipherList += " "

	print cipherList
	x += 1
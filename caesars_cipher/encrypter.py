# ==================================================================
# ========================= Caesars Cipher =========================
# ==================================================================
# ===========================  encrypter ===========================
# ==================================================================
# =========================  Murray Watson =========================
# ==================================================================

import os

class Main():
	global exit_choice;
	def exit_choice():
		os.system("clear")
		option = raw_input("would you like to exit?[y/n]: ").lower()

		if option == "y" or option == "yes":
			os.system("clear")
			exit()

		elif option == "n" or "no":
			getWord()

		else:
			option_error = raw_input("invalid option, use - y, yes, n or no")
			exit_choice()


	global getWord;
	def getWord():
		#gets the users word
		os.system("clear")
		users_word = raw_input("word or message: ").upper()

		try:
			users_key = int(raw_input("key: "))
			cipher(users_key, users_word)
				
		except ValueError:
			valueerror_msg = raw_input("the Key must be a number.")
			getWord()

	global cipher;
	def cipher(key, word):
		#implants the string with caesars cipher
		os.system("clear")
		if key > 25 or key == 0:
			keyerror = raw_input("key must be: > 0 & < 26")
			getWord()

		else:
			pass

		LAST_LETTER = 90
		numericList = []
		cipherList = []
		cipher_word = ""

		for c in word:
			numericList.append(ord(c))

		for i in numericList:
			if i in range(65, 91):
				pass

			elif i == 32:
				pass

			else:
				ILLEGAL_FOUND = raw_input("Please ensure you've only used - a-z, A-Z")
				getWord()

		for i in numericList:
			if chr(i + key) > chr(90):
				NEW_KEY = (i + key) - 26
				cipherList.append(chr(NEW_KEY))
				

			elif i != 32:
				cipherList.append(chr(i + key))

			elif i == 32:
				cipherList.append(" ")

		for c in cipherList:
			cipher_word += c

		print "PLAINTEXT - 	%s" % word
		print "CIPHER -	%s" % cipher_word

		pause = raw_input()

		exit_choice()
	getWord()
Main()
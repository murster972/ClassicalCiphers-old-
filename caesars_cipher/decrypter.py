# ==================================================================
# ========================= Caesars Cipher =========================
# ==================================================================
# ===========================  decrypter ===========================
# ==================================================================
# =========================  Murray Watson =========================
# ==================================================================

import os

class Main():
	global exit_choice;
	def exit_choice():
		#prompts users for exit
		os.system("clear")
		option = raw_input("would you like to exit[y/n] ").lower()

		if option == "y" or option == "yes":
			os.system("clear")
			exit()

		elif option == "n" or option == "no":
			getUsers()

		else:
			INVALID = raw_input("Inavlid choice.")
			exit_choice()

	global getUsers;
	def getUsers():
		#gets the users key and message
		os.system("clear")
		users_message = raw_input("message: ")
		users_message = users_message.lower()

		try:
			userse_key = int(raw_input("key: "))
			decrypt(userse_key, users_message)

		except ValueError:
			KEY_ERROR = raw_input("Please ensure the key is an integer.")
			getUsers()

	global decrypt;
	def decrypt(key, message):
		#decrypts the message
		os.system("clear")
		cipher_list = []
		PlainText_list = []
		plainText = ""

		for c in message:
			cipher_list.append(ord(c))
			
		for i in cipher_list:
			if i in range(97, 123):
				pass

			elif i == 32:
				pass

			else:
				ILLEGAL_FOUND = raw_input("Please ensure you've only used - a-z, A-Z")
				getUsers()

		for c in cipher_list:
			if chr(c - key) < chr(97):
				NEW_KEY = c + (26 - key)
				PlainText_list.append(NEW_KEY)

			elif c != 32:
				PlainText_list.append(c - key)

			else:
				pass

		for c in PlainText_list:
			plainText += chr(c)

		print "CIPHER -	%s" % message.upper()
		print "PLAINTEXT - 	%s" % plainText

		pause = raw_input("")

		exit_choice()

	getUsers()
Main()
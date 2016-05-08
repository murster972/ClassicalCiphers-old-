# ============================================================
# ================= Homophonic Substituation =================
# ============================================================
# ======================== Encryption ========================
# ============================================================
# ====================== Murray Watson  ======================
# ============================================================

from Crypto.Random import random
import os

class Main():
	global getMsg;
	def getMsg():
		#gets users word
		os.system("clear")
		message = raw_input("Message: ").upper()
		ILL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

		if len(message) < 1:
			LENERR = raw_input("Pleasee enter a valid message.")
			getMsg()

		else:
			encrypt(message)

	global encrypt;
	def encrypt(message):
		#encrypts the users word
		os.system("clear")
		substitutions = {
			"A": [07, 31, 50, 63, 66, 77, 84], 
			"B": [11, 64], 
			"C": [17, 33, 49], 
			"D": [10, 27, 51, 76], 
			"E": [25, 326, 28, 32, 48, 67, 69, 72, 75, 79, 82, 85], 
			"F": [99, 98], 
			"G": [44, 83], 
			"H": [19, 20, 21, 54, 70, 87], 
			"I": [02, 03, 29, 53, 68, 73], 
			"J": [18], 
			"K": [41],
			"L": [42, 81, 86, 95], 
			"M": [40, 52], 
			"N": [09, 43, 80], 
			"O": [16, 30, 61, 65, 91, 94, 96], 
			"P": [01, 62], 
			"Q": [15], 
			"R": [04, 24, 39, 58, 71, 26], 
			"S": [06, 34, 56, 57, 59, 90], 
			"T": [05, 23, 35, 37, 38, 60, 74, 78, 92], 
			"U": [13, 14, 36], 
			"V": [22],
			"W": [45, 46], 
			"X": [12], 
			"Y": [55, 93], 
			"Z": [47],
			" ": [97, 88, 89]
			}
		cipher_list = []
		cipher_word = ""
		
		for c in message:
			try:
				cl = random.choice(substitutions[c])
				cipher_list.append(int(cl))

			except KeyError:
				pass
					
		for c in cipher_list:
			cipher_word += str(c) + " "

		print "PLAINTEXT:   %s" % message
		print "CIPHER:      %s" % cipher_word

		pause = raw_input("")
		exit_choice()

	global exit_choice;
	def exit_choice():
		#prompts exit
		os.system("clear")
		EXIT = raw_input("would you like to exit?[y/n] ").lower()

		if EXIT == "y" or EXIT == "yes":
			os.system("clear")
			exit()

		elif EXIT == "n" or EXIT == "no":
			getMsg()

		else:
			try:
				INPUT_ERR = raw_input("Invalid choice.")
				exit_choice()

			except TypeError:
				exit_choice()

	getMsg()
Main()
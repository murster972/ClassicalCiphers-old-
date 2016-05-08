# -*- coding: utf-8 -*-
import os

class Main():
	global exitOpt;
	def exitOpt():
		#prompts user for exit
		os.system("clear")
		exit_opt = raw_input("woudl you like to exit? [y/n]: ").lower()

		if exit_opt == "y" or exit_opt == "yes":
			os.system("clear")

		elif exit_opt == "n" or exit_opt == "no":
			getMsg()

		else:
			INV_OPT = raw_input("Invalid option.")
			exitOpt()

	global getMsg;
	def getMsg():
		#gets the users message
		os.system("clear")
		punc = raw_input("would you like to inlcude punctuation in your message? [y/n]: ").lower()
		
		if punc == "y" or punc == "n" or punc == "yes" or punc == "no":
			pass

		else:
			INV_OPT = raw_input("Invalid option.")
			getMsg()

		os.system("clear")
		message = raw_input("message: ")

		if len(message) < 1:
			LEN_ERR = raw_input("Please enter a valid message.")
			getMsg()

		else:
			encrypt(message, punc)

	global encrypt;
	def encrypt(msg, punc):
		#encrypts the users message
		os.system("clear")
		upper_msg = msg.upper()
		cipher = {" ": " ", "A": "Z", "B": "Y", "C": "X", "D": "W", "E": "V", "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q", "K": "P", "L": "O", "M": "N", "N": "M", "O": "L", "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G", "U": "F", "V": "E", "W": "D", "X": "C", "Y": "B", "Z": "A"}
		cipher_msg = ""

		for i in upper_msg:
			try:
				cipher_letter = i.replace(i, cipher[i])
				cipher_msg += cipher_letter

			except KeyError:
				if punc == "y" or punc == "yes":
					cipher_msg += i

				else:
					pass

		print "PLAINTEXT - %s" % msg
		print "CIPHER -    %s" % cipher_msg

		pause = raw_input()
		exitOpt()

	getMsg()
Main()
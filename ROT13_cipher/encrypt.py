# -*- coding: utf-8 -*-
import os

class Main():
	global getMsg;
	def getMsg():
		#gets the users message
		os.system("clear")
		message = raw_input("message: ")

		if len(message) < 1:
			LEN_ERR = raw_input("Please enter a valid message.")
			getMsg()

		else:
			encrypt(message)

	global encrypt;
	def encrypt(msg):
		#encrypts the users message
		msg_upper = msg.upper()
		msg_list = []
		cipher_msg = ""

		for i in msg_upper:
			msg_list.append(ord(i))

		for i in msg_list:
			if chr(i + 13) > chr(90):
				NEW_KEY = (i + 13) - 26
				cipher_msg += chr(NEW_KEY)

			elif i != 32:
				if i < 65 or i > 90:
					pass

				else:
					cipher_msg += chr(i + 13)

			elif i == 32:
				cipher_msg += " "

		print cipher_msg
	getMsg()
Main()
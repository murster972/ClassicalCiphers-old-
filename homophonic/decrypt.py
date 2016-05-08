# ============================================================
# ================= Homophonic Substituation =================
# ============================================================
# ======================== Decryption ========================
# ============================================================
# ====================== Murray Watson  ======================
# ============================================================

import os

class Main():
	global getMsg;
	def getMsg():
		#gets the users msg
		os.system("clear")
		message  = raw_input("message: ")

		if len(message) < 1:
			LEN_ERR = raw_input("Please enter a valid message.")
			getMsg()

		else:
			for c in message:
				if c.isalpha() == True:
					if c == " ":
						pass

					else:
						ILL_CHR = raw_input("The message should only contain numeric values and spaces.")
						getMsg()

				else:
					pass

			decrypt(message)

	global decrypt;
	def decrypt(message):
		#decrypts the users message
		os.system("clear")
		PT = { "7": "A", "31": "A", "50": "A", "63": "A", "66": "A", "77": "A", "84": "A", "11": "B",  "64": "B", "17": "C", "33": "C", "49": "C", "10": "D", "27": "D", "51": "D", "76": "D", "25": "E", "326": "E", "28": "E", "32": "E", "48": "E", "67": "E", "69": "E", "72": "E", "75": "E", "79": "E", "82": "E", "85": "E", "99": "F", "98": "F", "44": "G", "83": "G", "19": "H", "20": "H", "21": "H", "54": "H", "70": "H", "87": "H", "2": "I", "3": "I", "29": "I", "53": "I", "68": "I", "73": "I", "18": "J", "41": "K", "42": "L", "81": "L", "86": "L", "95": "L", "40": "M", "52": "M", "9": "N", "43": "N", "80": "N", "16": "O", "30": "O", "61": "O", "65": "O", "91": "O", "94": "O", "96": "O", "1": "P", "62": "P", "15": "Q", "4": "R", "24": "R", "39": "R", "58": "R", "71": "R", "26": "R", "6": "S", "34": "S", "56": "S", "57": "S", "59": "S", "90": "S", "5": "T", "23": "T", "35": "T", "37": "T", "38": "T", "60": "T", "74": "T", "78": "T", "92": "T", "13": "U", "14": "U", "36": "U", "22": "V", "45": "W", "46": "W", "12": "X", "55": "Y", "93": "Y", "47": "Z", "97": " ","88": " ", "89": " ",}
		cipher_char = str(message).split()
		PLAINTEXT = ""

		for c in cipher_char:
			try:
				plain_char = c.replace(c, PT[c])
				PLAINTEXT += plain_char

			except KeyError:
				pass

		print "CIPHER:      %s" % message
		print "PLAINTEXT:   %s" % PLAINTEXT

		pause = raw_input("")

		exit_option()

	global exit_option;
	def exit_option():
		#prompts the user for exit
		os.system("clear")
		option = raw_input("would you like to exit?[y/n]").lower()

		if option == "y" or option == "yes":
			os.system("clear")
			exit()

		elif option == "n" or option == "no":
			getMsg()

		else:
			INV_OPT = raw_input("invalid option.")
			exit_option()

	getMsg()
Main()
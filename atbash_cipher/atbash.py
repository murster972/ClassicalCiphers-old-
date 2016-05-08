import os

class Atbash(object):
	def __init__(self, msg, oper):
		self.msg = msg
		self.oper = oper

	def ValidateMsg(self):
		opers = {"ENCRYPT": lambda: Atbash.Encrypt(self), "DECRYPT": lambda: Atbash.Decrypt(self)}

		for x in range(len(self.msg) + 1):
			if x < len(self.msg):
				check = ord(self.msg[x])

				if check < 65 or check > 90:
					print "Invalid Message."
					pause = raw_input()
					main()
					break

				else:
					pass

			else:
				opers[self.oper]()

	def Encrypt(self):
		cipherText = ""

		"""if chr(i + 13) > chr(90):
				NEW_KEY = (i + 13) - 26
				cipher_msg += chr(NEW_KEY)"""

		for x in range(len(self.msg)):
			msgChr = ord(self.msg[x])
			
			if chr(msgChr + 13) > chr(90):
				cipherText += chr((msgChr + 13) - 26)

			else:
				cipherText += chr(msgChr + 13)

		print "Plain Text: %s\nCipher Text: %s" % (self.msg, cipherText)
		pause = raw_input()
		main()

	def Decrypt(self):
		plainText = ""

		for x in range(len(self.msg)):
			msgChr = ord(self.msg[x])
			
			if chr(msgChr - 13) < chr(65):
				plainText += chr((msgChr - 13) + 26)

			else:
				plainText += chr(msgChr - 13)

		print "Cipher Text: %s\nPlain Text: %s" % (self.msg, plainText)
		pause = raw_input()
		main()
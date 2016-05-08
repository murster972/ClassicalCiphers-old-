class Encrypt(object):
	def __init__(self, key, word):
		self.key = key
		self.word = word

	def errors(self, error):
		print error
		pause = raw_input()

	def encrypt(self):
		if self.key > 25 or self.key == 0:
			super(Encrypt, self).errors("key must be: > 0 & < 26")

		else:
			LAST_LETTER = 90
			numericList = []
			cipherList = []
			cipher_word = ""

			for c in self.word:
				numericList.append(ord(c))

			for i in numericList:
				if i in range(65, 91):
					pass

				elif i == 32:
					pass

				else:
					pass

			for i in numericList:
				if chr(i + self.key) > chr(90):
					NEW_KEY = (i + self.key) - 26
					cipherList.append(chr(NEW_KEY))
					

				elif i != 32:
					cipherList.append(chr(i + self.key))

				elif i == 32:
					cipherList.append(" ")

			for c in cipherList:
				cipher_word += c

			return "Plain Text: %s\nCipher Text: %s" % (self.word, cipher_word)

test = Encrypt(12, "Hey")
print test.encrypt()
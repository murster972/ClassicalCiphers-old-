#!/usr/env/bin python
"""
	Bifid Cipher: A classical cipher that combines the polybius square with
	transposition, and uses fractionation to achieve diffusion
"""
import os
import random

class BifidCipher(object):
	def __init__(self, msg, values={}):
		self.msg = msg
		self.values = values
		self.alph = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
		self.validate_msg()
		self.create_table()

	""" 
		Validates msg: removes any illegal chars, changes to upper case and combines
		'J' and 'I'.
	"""
	def validate_msg(self):
		self.msg = self.msg.upper().replace("J", "I")

		for i in self.msg:
			if self.alph.find(i) == -1:
				self.msg = self.msg.replace(i, "")

	""" Creates Table: Checks if values have been provided, if no values
		have been provdied then values are created for ecnryption, if values are
		provided it checks if they're valid and then decrypts if they are, else
		an error is displyed.
	"""
	def create_table(self):
		if len(self.values) == 0:
			alph = [x for x in self.alph]
			random.shuffle(alph)

			row_col = "12345"
			rows = [alph[x:x + 5] for x in range(0, 25, 5)]
			coords = {}

			for i in range(5):
				for j in range(5):
					coords[rows[i][j]] = row_col[i] + row_col[j]

			self.values = coords
			self.encrypt()

		elif len(self.values) == 25:
			try:
				test = [self.values[x] for x in self.alph]
				self.decrypt()

			except KeyError and TypeError:
				print "Invalid Values!"

		else:
			print "Invalid values!"

	"""
		Encrypts the users message: using the values created or provided, msg is first
		converted to it's coordinates in 'self.values'. The first coords of each char
		is then put into a list and the second coord another, the coords are then put
		into pairs using each separate list, and translated into there following values
		using the values in 'self.values'.
	"""
	def encrypt(self):
		char_coords = [self.values[x] for x in self.msg]
		coords_top = [x[0] for x in char_coords]
		coords_botm = [x[1] for x in char_coords]
		coord_pairs = []

		for i in range(0, len(coords_top) - 1, 2):
			coord_pairs.append(coords_top[i] + coords_top[i + 1])

		for i in range(0, len(coords_botm) - 1, 2):
			coord_pairs.append(coords_botm[i] + coords_botm[i + 1])

		reveresed_values = {}

		for i in self.values:
			reveresed_values[self.values[i]] = i

		cipher_text = ""

		for i in coord_pairs:
			cipher_text += reveresed_values[i]

		print "CIPHERTEXT: %s" % cipher_text
		print "VALUES: %s" % self.values
		raw_input()

	"""
		Decrypts the users message: the users message is decrypted by doing 'encrypt' in
		reverse order.
	"""
	def decrypt(self):
		coords = [self.values[x] for x in self.msg]
		coord_rows = [x for i in coords for x in i]
		coords_top = [coord_rows[x] for x in range(len(self.msg))]
		coords_bottom = [coord_rows[x] for x in range(len(self.msg), len(coord_rows))]
		plaintext_coords = [(coords_top[x] + coords_bottom[x]) for x in range(len(self.msg))]		

		reveresed_values = {}

		for i in self.values:
			reveresed_values[self.values[i]] = i

		plaintext = ""

		for i in plaintext_coords:
			plaintext += reveresed_values[i]

		print "PLAINTEXT: %s" % plaintext
		raw_input()

def main():
	os.system("clear")
	test_msg = "Hello World!"
	test_values = {'A': '52', 'C': '42', 'B': '33', 'E': '51', 'D': '23', 'G': '15', 'F': '21', 'I': '34', 'H': '41', 'K': '13', 'M': '45', 'L': '53', 'O': '22', 'N': '31', 'Q': '44', 'P': '35', 'S': '12', 'R': '54', 'U': '32', 'T': '25', 'W': '55', 'V': '43', 'Y': '24', 'X': '11', 'Z': '14'}
	test_cipher = "MWTTAXBTYB"
	BifidCipher(test_cipher)

if __name__ == '__main__':
	main()
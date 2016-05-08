dffbdfb#!/usr/bin/evn python
import os
import random

class OneTimePad():
	def __init__(self, msg):
		self.msg = msg
		self.pad = self.gen_pad()
		self.alph_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}
		self.alph_dict_reverse = {}

		for x in self.alph_dict:
			self.alph_dict_reverse[self.alph_dict[x]] = x

	def gen_pad(self):
		alph = [x for x in "abcdefghijklmnopqrstuvwxyz".upper()]
		random.shuffle(alph)
		pad = ""

		for i in range(len(self.msg)):
			pad += alph[random.randint(0, 25)]

		return pad

	def encrypt(self):
		msg_vals = [self.alph_dict[x] for x in self.msg]
		key_vals = [self.alph_dict[x] for x in self.pad]
		ciphertext_vals = [((msg_vals[x] + key_vals[x]) % 26) for x in range(len(self.msg))]
		ciphertext = ""

		for x in ciphertext_vals:
			ciphertext += self.alph_dict_reverse[x]

		return (ciphertext, self.pad)

	def decrypt(self, pad):
		cipher_vals = [self.alph_dict[x] for x in self.msg]
		key_vals = [self.alph_dict[x] for x in pad]
		plaintext_vals = [((cipher_vals[x] - key_vals[x]) % 26) for x in range(len(self.msg))]
		plaintext = ""

		for x in plaintext_vals:
			plaintext += self.alph_dict_reverse[x]

		return plaintext

if __name__ == '__main__':
	test_msg = "helloworld".upper()
	test_cipher = "EAOLADBFYE"
	test_pad = "XWDAMHNONB"
	cipher, pad = OneTimePad(test_msg).encrypt()
	print "pad: " + pad
	print "cipher: " + cipher
	plaintext = OneTimePad(test_cipher).decrypt(test_pad)
	print "plaintext: " + plaintext
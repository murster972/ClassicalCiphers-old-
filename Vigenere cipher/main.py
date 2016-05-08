#!/usr/bin/env python
import os

class VigenereCipher(object):
	def __init__(self, msg, key):
		self.msg = msg
		self.key = key.upper()
		self.alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.table_values = {}
		self.create_table()
		self.full_key()
		self.validate_msg()
		self.encrypt()

	def validate_msg(self):
		self.msg = self.msg.upper()

		for i in self.msg:
			if self.alph.find(i) == -1:
				self.msg = self.msg.replace(i, "")

	def create_table(self):
		rows = [self.alph[x:] + self.alph[:x] for x in range(26)]

		for i in range(26):
			for j in range(26):
				value = self.alph[i] + self.alph[j]
				self.table_values[value] = rows[i][j]

	def full_key(self):
		key = ""
		i = 0

		while len(key) != len(self.msg):
			if i == len(self.key):
				i = 0
				key += self.key[i].upper()

			else:
				key += self.key[i].upper()

			i += 1

		self.key = key

	def encrypt(self):
		ciphertext = ""

		for i in range(len(self.msg)):
			ciphertext += self.table_values[self.msg[i] + self.key[i]]

		print ciphertext

	def decrypt(self):
		rows = [self.alph[x:] + self.alph[:x] for x in range(26)]
		table_dict = {}

		for i in range(26):
			cur_row = rows[i]
			row_dict = {}

			for j in range(26):
				row_dict[cur_row[j]] = self.alph[j]

			table_dict[self.alph[i]] = row_dict

		plaintext = ""

		for i in range(len(self.msg)):
			cur_row = table_dict[self.key[i]][self.msg[i]]
			plaintext += cur_row

		print plaintext


if __name__ == '__main__':
	#os.system("clear")
	test_msg = "Fucking foreign langauges"
	test_cipher = "LXFOPVEFRNHR"
	test_key = "klasdm"
	VigenereCipher(test_msg, test_key)
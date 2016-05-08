#!/usr/bin/env python
import os
import random

class ADFGVXCipher(object):
	def __init__(self, msg, key, table={}):
		self.msg = msg
		self.key = key
		self.table = table
		self.alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
		self.validate_msg()
		self.create_table()

	def validate_msg(self):
		self.msg = self.msg.upper()

		for i in self.msg:
			if self.alph.find(i) == -1:
				self.msg = self.msg.replace(i, "")

	def create_table(self):
		if len(self.table) == 0:
			col_row = "ADFCVX"
			random_alph = [x for x in self.alph]
			random.shuffle(random_alph)
			rows = []

			for i in range(0, 36, 6):
				rows.append(random_alph[i:i+6])

			for i in range(6):
				for j in range(6):
					self.table[rows[i][j]] = col_row[i] + col_row[j]

			self.encrypt()

		elif len(self.table) == 36:
			#check if values are valid
			pass

		else:
			#value provided but not valid
			pass

	def encrypt(self):
		msg_coords = [self.table[x] for x in self.msg]
		key_rows = []
		cur_row = []

		for i in range(len(msg_coords)):
			if len(cur_row) == len(self.key) - 1:
				cur_row.append(msg_coords[i])
				key_rows.append(cur_row)
				cur_row = []

			else:
				cur_row.append(msg_coords[i])

		print key_rows


	def decrypt(self):
		pass

if __name__ == '__main__':
	os.system("clear")
	test_msg = "Attack at Dawn!"
	test_key = "Private"
	#ADFGVXCipher(test_msg, test_key)
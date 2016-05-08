#!/usr/bin/env python
import os
import math

class RSA(object):
	def __init__(self, test_msg):
		self.gen_keys()

	def change_msg(self):
		pass
	
	def gen_keys(self):
		p = 5	#gen_primes()
		q = 11	#gen_primes()
		n = p * q
		totient_n = (p - 1) * (q - 1)
		e = 7

	def gen_primes(self):
		pass

	def rel_primes(self, totient_n):
		pass

	def encrypt(self):
		pass

	def decrypt(self, pub_key=0, pri_key=0):
		pass

if __name__ == '__main__':
	test_msg = "Hello World!"
	RSA(test_msg)
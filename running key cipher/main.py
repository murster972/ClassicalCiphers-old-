#!/usr/bin/env python
""" Running Key Cipher """
import os

def encrypt(msg, key):
	print msg

def decrypt(msg, key):
	pass

def verify_msg(msg):
	legal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	msg = msg.upper()

	for i in msg:
		if legal.find(i) == -1:
			msg = msg.replace(i, "")

	return msg

def main():
	os.system("clear")
	test_msg = "flee at once!"
	test_msg = verify_msg(test_msg)
	test_key = "thisisatestkey"
	encrypt(test_msg, test_key)

if __name__ == '__main__':
	main()
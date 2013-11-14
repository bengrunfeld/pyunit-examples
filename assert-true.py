#! /usr/bin/python

import unittest

class TestSequenceFunctions(unittest.TestCase):

	def create_true_return_val(self, x):
		if x > 9:
			return True

	def test_exception(self):
		#This check tests if a condition is TRUE
		self.assertTrue(self.create_true_return_val(10))

if __name__ == '__main__':
	unittest.main()
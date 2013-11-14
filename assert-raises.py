#! /usr/bin/python

import unittest

class TestSequenceFunctions(unittest.TestCase):

	def setUp(self):
		self.errorVar = 10

	def test_create_exception(self, x):
		self.errorVar = x

	def test_assert_raises(self):
		#This check tests if a specific exception was raised
		self.assertRaises(SyntaxError, test_create_exception, '10p')

if __name__ == '__main__':
	unittest.main()
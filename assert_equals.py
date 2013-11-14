#! /usr/bin/python

import unittest

class TestSequenceFunctions(unittest.TestCase):

	def setUp(self):
		self.someVar = 10

	def test_some_var(self):
		#This simply tests the value of the variable
		self.assertEqual(self.someVar, 10)

if __name__ == '__main__':
	unittest.main()
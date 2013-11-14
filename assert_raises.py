#! /usr/bin/python
"""This program tests the assertRaises function of PyUnit"""

import unittest

class TestSequenceFunctions(unittest.TestCase):

	def create_exception(self, x):
		self.errorVar = x

	def test_exception(self):
		"""This check tests if a specific exception was raised"""
		self.assertRaises(SyntaxError, self.create_exception('10p'))

if __name__ == '__main__':
	unittest.main()
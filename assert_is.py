#! /usr/bin/python
"""This program tests the assertIs function of PyUnit"""

import unittest

class Employee:
	def __init__(self):
		self.someVar = range(10)

dave = Employee()
mike = Employee()
matt = dave

class TestSequenceFunctions(unittest.TestCase):

	def test_is(self):
		"""This check tests if the two objects are the same"""
		self.assertIs(dave, matt)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
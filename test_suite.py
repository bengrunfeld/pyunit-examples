#! /usr/bin/python
"""This program illustrates the use of the Test Suite feature of PyUnit"""

import unittest

class Employee:
	def __init__(self):
		self.someRange = range(10)

dave = Employee()
mike = Employee()
matt = dave

class Volunteer:
	def __init__(self):
		self.someRange = range(10)

class TestSequenceFunctions(unittest.TestCase):

	def test_is(self):
		"""This check tests if the two objects are the same"""
		self.assertIs(dave, matt)

	def test_is_not(self):
		"""This check tests if the two objects are not the same"""
		self.assertIsNot(dave, mike)

def suite():
	suite = unittest.TestSuite()
	suite.addTest(TestSequenceFunctions('test_is'))
	suite.addTest(TestSequenceFunctions('test_is_not'))
	return suite

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)

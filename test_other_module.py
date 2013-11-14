#! /usr/bin/python
"""This program tests a separate module - module-being-tested.py, thus separating test code from shipped code"""

import unittest
import module_being_tested

class TestSequenceFunctions(unittest.TestCase):

	def test_is(self):
		"""This check tests if a condition is TRUE in module-being-tested.py"""
		self.assertTrue(module_being_tested.dave, module_being_tested.mike)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
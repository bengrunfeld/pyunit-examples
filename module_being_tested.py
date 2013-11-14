#! /usr/bin/python
"""This program is being tested by a separate module (test-other-module.py), thus separating test code from shipped code"""

class Employee:
	def __init__(self):
		self.someRange = range(10)

dave = Employee()
mike = Employee()
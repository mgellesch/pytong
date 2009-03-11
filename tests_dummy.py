#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest, time

class MySuite(unittest.TestCase):
	def setUp(self):
		print "setUp"
	def tearDown(self):
		print "tearDown"
	def test_ok(self):
		time.sleep(2)
		print "test_ok"
		self.assert_(True)
	def test_ok2(self):
		time.sleep(2)
		print "test_ok2"
		self.assert_(True)
		

class MySuite2(unittest.TestCase):
	def setUp(self):
		print "setUp"
	def tearDown(self):
		print "tearDown"
	def test_ok(self):
		time.sleep(2)
		print "MySuite2_test_ok"
		self.assert_(True)
	def test_nok(self):
		time.sleep(2)
		print "MySuite2_test_nok"
		self.assert_(False)

if __name__ == "__main__":
	unittest.main()

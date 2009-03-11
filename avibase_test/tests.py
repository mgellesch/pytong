#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import selenium
import unittest, time, re, random
import subprocess, httplib, os

# pages: dict with key, value = (url, indicator)
pages = {"home": ("avibase.jsp", "//h2[contains(.,'Welcome to Avibase')]"),
		 "checklist": ("checklist.jsp", "//h2[contains(.,'Bird Checklists')]"),
		}
host = "localhost"
port = 4444
server = False

class SeleniumTest(unittest.TestCase):
	def setUp(self):
		global server
		if not server and not canConnect(host, port):
			self.serverProcess = subprocess.Popen(["java", "-jar", "selenium-server-1.0-beta-2/selenium-server.jar"])
		waitForConnection(host, port)
		server = True
		self.verificationErrors = []
		browser = "*iexplore"
		if hasattr(os, "uname") and os.uname()[0] == "Darwin":
			browser = "*safari"
		self.selenium = selenium(host, port, browser, "http://avibase.bsc-eoc.org")
		self.selenium.start()
		self.selenium.window_maximize()
		self.selenium.set_speed(2000)

	def tearDown(self):
		self.selenium.stop()
		return 

	def testSearch(self):
		self.selenium.open("/")
		self.type_focus("//input[@name='qstr' and @size='30']", "swael")
		self.click_and_wait("//input[@value='Go']")
		# Test if the Plain Martin (Riparia paludicola) is found
		self.click_and_wait("link=Riparia paludicola")
		# This bird's order should be 'Passeriformes'.
		self.assert_(self.selenium.is_text_present('Passeriformes'), "Text 'Passeriformes' not present.")

	def testChecklist(self):
		self.selenium.open("/")
		self.goto("checklist")
		self.click_and_wait('link=Sint-Eustatius')
		# Check if the Red tailed hawk lives in Sint-Eustatius
		self.assert_(self.selenium.is_text_present('Buteo jamaicensis'))

	def testLanguages(self):
		self.selenium.open("/")
		self.assert_(self.selenium.is_text_present('Welcome to Avibase'))
		self.click_and_wait("link=Spanish")
		self.assert_(self.selenium.is_text_present('Bienvenido a Avibase'))
		self.click_and_wait("link=afrikaans")
		self.assert_(self.selenium.is_text_present('Welkom by Avibase'))
		self.click_and_wait("link=Interlingua")
		self.assert_(self.selenium.is_text_present('Benvenite a Avibase'))

	def click_and_wait(self, selector, checkErrors = False):
		self.selenium.focus(selector)
		self.selenium.click(selector)
		self.selenium.wait_for_page_to_load("5000")

	def type_focus(self, locator, value):
		self.selenium.focus(locator)
		self.selenium.type(locator, value)

	def onPage(self, page):
		"""Returns True if we are on the requested page."""
		url, indicator = pages[page]
		return sel.is_element_present(indicator)

	def assertOnPage(self, page):
		self.assert_(self.onPage(page), "Not on page: %s" % page)

	def goto(self, page):
		"""Follow a link to a web page and verify the page."""
		url, indicator = pages[page]
		self.click_and_wait("//a[contains(@href, '/%s')]" % url)
		self.failUnless(self.selenium.is_element_present(indicator))

def canConnect(host, port):
	c = httplib.HTTPConnection(host, port)
	try:
		c.connect()
	except httplib.socket.error, e:
		return False
	c.close()
	return True

def waitForConnection(host, port):
	for i in range(10):
		if canConnect(host, port):
			return
	print "Could not connect to server."
	raise httplib.socket.error
	
if __name__ == "__main__":
	unittest.main()

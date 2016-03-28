__author__ = 'nicholas.redmond'
# import os
# os.system("pip install --user selenium")

import unittest
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException


class ContactPageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def test_schedule_demo_label_visible(self):
        self.driver.get("https://www.dealertrack.com")
        self.driver.find_element(By.XPATH, ".//*[@id='bs-example-navbar-collapse-1']//*[contains(@href, '/contact.html')]").click()

        element = None
        try:
            element = self.driver.find_element(By.XPATH, ".//*[text()='Schedule a Product Demo']")
        finally:
            if not (element and element.is_displayed()):
                raise ElementNotVisibleException("Product Demo label was not visible.")

    def tearDown(self):
        self.driver.close()

output_file = open('reports/html/index.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=output_file, title="Nick Redmond's First HTML Output",
                                       description="This is a test of HTML output in Python automated tests.")

suite = unittest.TestSuite()
suite.addTest(ContactPageTests("test_schedule_demo_label_visible"))
runner.run(suite)

__author__ = 'nicholas.redmond'
import os
os.system("pip install --user selenium")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.dealertrack.com")
driver.find_element(By.XPATH, ".//*[@id='bs-example-navbar-collapse-1']//*[contains(@href, '/contact.html')]").click()

driver.find_element(By.XPATH, ".//*[text()='Schedule a Product Demo']").is_displayed()
driver.quit()
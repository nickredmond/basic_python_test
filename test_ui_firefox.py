__author__ = 'nicholas.redmond'
# import os
# os.system("pip install --user selenium")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.dealertrack.com")
driver.find_element(By.XPATH, ".//*[@id='bs-example-navbar-collapse-1']//*[contains(@href, '/contact.html')]").click()

element = None
try:
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(By.XPATH, ".//*[text()='Schedule a Product Demo']")
    # )
    element = driver.find_element(By.XPATH, ".//*[text()='Schedule a Product Demo']")
finally:
    if not (element and element.is_displayed()):
        raise ElementNotVisibleException("Product Demo label was not visible.")

driver.quit()
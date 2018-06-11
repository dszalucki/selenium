from selenium import webdriver
from selenium.webdriver.common.by import By
from window import Okno

import os


Okno().uwierzytelnianie()

driverlocation = 'C:\\Users\Darek\PycharmProjects\LIBRARY\chromedriver'
os.environ["webdriver.chrome.driver"] = driverlocation
driver = webdriver.Chrome(driverlocation)

driver.get("https://online.mbank.pl/pl/Login")

driver.find_element(By.ID, 'userID').send_keys(Okno.login)
driver.find_element(By.ID, "pass").send_keys(Okno.haslo)

driver.find_element(By.ID, 'submitButton').click()

driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//*[@id="main-nav"]/ul/li[1]/ul/li[3]/a').click()
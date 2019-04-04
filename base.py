# Imports
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lISimplifier import tD, uH, sK1, pT, lH, sS, sB, pB, cR, dT, sK, tDx, uN, pW, fT, tDy, jj, lI


askKey = input('What would you like to share? ')  # Non-input> askKey = 'Etc...'
print('Ok, on it. ')
now = time.time()


driver = webdriver.Firefox()  # Que vámonos
driver.get(lI)  # loading LinkedIn
sleep(tD)


userInput = driver.find_element(By.XPATH, uH)  # Logging in
userInput.send_keys(uN)  # Username
sleep(tD)
passInput = driver.find_element(By.XPATH, pT)  # Password
passInput.send_keys(pW)
sleep(tD)
signInInput = driver.find_element(By.XPATH, lH)  # 'Sign in' button
signInInput.click()
sleep(tDy)


driver.get(lI)  # Reload to allow page load independent speed
sleep(tDy)
shareElement = driver.find_element(By.XPATH, sS)  # Status time
shareElement.click()
sleep(tD)
shareHere = driver.find_element(By.XPATH, sB)
shareHere.send_keys(askKey, jj, sK, cR, dT, sK1, Keys.RETURN)
sleep(tDx)  # Delay to load link preview
sleep(100)
sendIt = driver.find_element(By.XPATH, pB)
sendIt.click()
sleep(tDy)


then = time.time()
print(fT, jj, then - now, jj, 'seconds')

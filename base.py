# Imports
from time import sleep
from userinfo import user, pwrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def post(username, password, status='ask', link='ask', test=False):
    """
    posts to LinkedIn using Selenium webdriver (GeckoDriver)
    """
    if test==True:
        # import
        import time
        # set start 
        now = time.time()

    if status == 'ask':
        link = input('status: ')
    
    """NOT WORKING RIGHT NOT ; REASON UNKNOWN"""
    if link == 'ask':
        link = input('link: ')

    sleep(100)

    driver = webdriver.Firefox()  # Que vámonos
    driver.get('https://linkedin.com/login')  # loading LinkedIn
    sleep(3)

    # login button
    userInput = driver.find_element(By.XPATH, '//*[@id="username"]')  
    userInput.send_keys(username)  
    sleep(1)

    # password box
    passInput = driver.find_element(By.XPATH, '//*[@id="password"]')  
    passInput.send_keys(password)
    sleep(1)

    # sign in button
    signInInput = driver.find_element(By.XPATH, '/html/body/div/main/div/form/div[3]/button')  
    signInInput.click()
    sleep(2)

    # reload & sleep to allow page load independent speed
    driver.get('https://linkedin.com')  
    sleep(3)

    # small status box
    shareElement = driver.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[3]/div/div/div/div/div[1]/div/div[1]/button')  
    shareElement.click()
    sleep(3)

    # where to send status (open satus box)
    shareHere = driver.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[3]/div/div/div/div/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/p')
    # link or not
    if link==False:
        shareHere.send_keys(status)
    else:
        shareHere.send_keys(status, ' ', link, Keys.RETURN)
    sleep(5)  

    if test=='untimed':
        sleep(100000)
        # ^that's a while
    
    # finalize post
    sendIt = driver.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[3]/div/div/div/div/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]')
    sendIt.click()

    # wait and exit
    sleep(5)
    driver.quit()

    # test info
    if test==True:
        then = time.time()
        print(f'{then - now} seconds')

# check that username and password are logical
if len( user ) < 1 or len( pwrd ) < 1:
    raise Exception('illogical username or password\nplease check you have correctly entered your login information \n@ login_info.py\n'
                    f'current user = {user} (len={len(user)})\ncurrent password = {pwrd} (len={len(pwrd)})') 

# option to enter username upon call
if user == '__OPT-OUT__':
    user = input('username: ')

# option to enter password upon call
if pwrd == '__OPT-OUT__':
    pwrd = input('password: ')

# check that username and password are logical
if len( user ) < 1 or len( pwrd ) < 1:
    raise Exception('illogical username or password\nplease check you have correctly entered your login information \n@ login_info.py\n'
                    f'current user = {user} (len={len(user)})\ncurrent password = {pwrd} (len={len(pwrd)})') 

# let's post
post(user, pwrd, status='ask', link='ask', test=True)

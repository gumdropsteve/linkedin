from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from paths import login_page, user_box, pass_box, start_share_button, to_talk_about, post_button
from userinfo import user, pwrd


class LinkedOut:    
    '''
    simple overview:
        1) open browser
        2) log in to LinkedIn
        3) locate & engage 'Share a post' box
        4) send post (keys) to post box
        5) post update & get outta dodge 
    note: 
        sleep included for loadtimes
    required inputs:
        > email or phone number (username) 
        > password (not explaining)
        > webdriver (selenium; e.g. gecko, chrome, edge)
    '''

    # kicking off
    def __init__(self, username, password, driver):
        '''
        inputs)
            1) self
                >> self (oop)
            2) username
                >> email or phone number of account posting
            3) password
                >> password of account posting
            4) driver
                >> WebDriver of choice 
        '''
        # set user
        self.u = username
        # set pwrd
        self.p = password
        # set driver
        self.driver = driver
    
    # regarding logging in 
    def login(self):
        '''
        process)
            > note and minimize browser (driver) window
            > load LinkedIn's login page 
            > log in to LinkedIn 
                >> email/phone then password + enter 
                    > does not require click of login button  
        '''
        # tag driver
        driver = self.driver

        # minimize browser to shied our eyes 
        driver.minimize_window()
        # load login page
        driver.get(login_page) 
        # take a breath (hedge load time)
        sleep(1)

        # identify and send username to user input box
        driver.find_element_by_xpath(user_box).send_keys(self.u)
        # take a breath (hedge type time)
        sleep(1)

        # identify and send password (& then return) to pwrd input box
        driver.find_element_by_xpath(pass_box).send_keys(self.p, Keys.RETURN)
        # give keys time to land and site a bit to process login request 
        sleep(5)
    
    # regarding sharing the post 
    def share_the_post(self, post):
        '''
        inputs)
            > self
                >> oop
            > post
                >> post being shared
        process)
            > note driver, note post
            > click to 'Share a post'
            > type out the post
            > click 'Post' button to share the post 
        '''
        # tag driver
        driver = self.driver
        # init/set status 
        self.post = post
        
        # id and click 'Share a post' button
        driver.find_element_by_css_selector(start_share_button).click()
        # give the site a second to load
        sleep(1)
        
        # find and send status to 'Share a post' input box 
        driver.find_element_by_css_selector(to_talk_about).send_keys(self.post)
        # time for post to be typed out
        sleep(2)

        # locate and click 'Post' button
        driver.find_element_by_xpath(post_button).click()
        # allow site to process post request & load visable proof 
        sleep(5)
    
    def we_done(self):
        '''
        close any browser windows & safely end the session   
        '''
        # shut down shop for the night
        self.driver.quit()


# make this a runable script 
if __name__ == "__main__":

    # username 
    user_id = user
    # password
    pword = pwrd

    # option to input email/phone live
    if user_id == '__OPT-OUT__':
        # ask for user
        ask = input('username: ')
        # reset user
        user_id = ask
    # option to input password live
    if pword == '__OPT-OUT__':
        # ask for pwrd
        ask = input('password: ')
        # reset pwrd
        pword = ask

    # Firefox/Gecko options setup
    options = webdriver.FirefoxOptions()  
    # deactivate push notifications
    options.set_preference('dom.push.enabled', False)   

    # request post for sharing 
    status = input('What would you like to share? ')

    # tag bot
    incoming = LinkedOut(user_id, pword, webdriver.Firefox(options=options))

    # get the party started 
    incoming.login()

    # share the post
    incoming.share_the_post(post=status)    

    # get the heck outta dodge 
    incoming.we_done()
    # and give reassurance so we don't engage the void
    print(f'sent {status}\nto account associated with {user}')

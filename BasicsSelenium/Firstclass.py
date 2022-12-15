import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class firstclass():

    def firstclassimplementation(self):
        #browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        browser.get("https://www.facebook.com/") #add some in to the adress bar
        browser.maximize_window()
        #username=browser.find_element(by=By.ID,value="email")
        #username = browser.find_element(by=By.NAME, value="email")
        #username = browser.find_element(by=By.CLASS_NAME, value="inputtext _55r1 _6luy")
        #username = browser.find_element(by=By.CSS_SELECTOR, value="input#email") #tag#id
        #username = browser.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1 _6luy")  # tag.class
        #username = browser.find_element(by=By.CSS_SELECTOR, value="input[data-testid=royal_email]")  # tag[atribute=value]
        #username = browser.find_element(by=By.CSS_SELECTOR,value="input.inputtext _55r1 _6luy[data-testid=royal_email]")  # tag.class[atribute=value]
        #username = browser.find_element(by=By.XPATH,value="//input[@id='email']")
        username = browser.find_element(by=By.XPATH, value="//*[contains(@class,'_55r1') and @data-testid='royal_email' or @name='email']")
        username.send_keys("kumar.sathish189@")
        time.sleep(1)
        username.clear()
        browser.find_element(by=By.ID, value="email").send_keys("sathish")
        browser.find_element(by=By.ID, value="email").send_keys("besant")
        #browser.find_element(by=By.XPATH,value="//button[contains(@id,'u_0_9')]").click()
        browser.find_element(by=By.XPATH,value="//*[starts-with(@id,'u_0_9')]").click()
        #browser.find_element(by=By.LINK_TEXT,value="Forgotten password?").click()
        browser.find_element(by=By.PARTIAL_LINK_TEXT, value="pass").click()
        #browser.minimize_window()
        #browser.set_window_size(1200,1200)
        #browser.refresh()
        #browser.get("https://www.gmail.com/")
        #browser.back()
        #browser.forward()
        time.sleep(3)

obj=firstclass()
obj.firstclassimplementation()
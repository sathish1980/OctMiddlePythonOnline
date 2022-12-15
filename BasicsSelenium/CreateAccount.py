import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class createaccount():

    def createaccountimplementation(self):
        browser = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        browser.get("https://www.facebook.com/")  # add some in to the adress bar
        browser.maximize_window()
        browser.find_element(by=By.XPATH,value="//*[@data-testid='open-registration-form-button']").click()
        browser.implicitly_wait(60)
        browser.find_element(by=By.NAME,value="firstname").send_keys("sathish")
        browser.find_element(by=By.XPATH,value="(//*[contains(@class,'_8ien')]//img)[1]").click()
        browser.find_element(by=By.XPATH, value="//*[@data-testid='open-registration-form-button']").click()
        browser.find_element(by=By.NAME, value="firstname").send_keys("sathish")
        browser.find_element(by=By.XPATH,value="//*[@data-name='gender_wrapper']//span[3]//input").click()
        #explict wait
        WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.NAME, "preferred_pronoun")))
        browser.find_element(by=By.NAME, value="preferred_pronoun").click()
        time.sleep(2)


obj=createaccount()
obj.createaccountimplementation()
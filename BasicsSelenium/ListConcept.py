import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class listconcept():

    global driver
    def listimplementation(self,actualcounryname):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://leafground.com/select.xhtml")
        self.driver.maximize_window()
        CountryList=self.driver.find_element(by=By.ID,value="j_idt87:country")
        CountryList.click()
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='j_idt87:country_items']//li[1]")))
        Allcountries=self.driver.find_elements(by=By.XPATH,value="//*[@id='j_idt87:country_items']//li")
        print(len(Allcountries))
        for eachvalue in Allcountries:
            countryname=eachvalue.text
            if countryname==actualcounryname:
                eachvalue.click()
                break
        time.sleep(2)

    def listimplementationcity(self,actualcityname):
        CityList=self.driver.find_element(by=By.ID,value="j_idt87:city")
        CityList.click()
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='j_idt87:city_items']//li[1]")))
        Allcities=self.driver.find_elements(by=By.XPATH,value="//*[@id='j_idt87:city_items']//li")
        print(len(Allcities))
        for eachcityvalue in Allcities:
            cityname=eachcityvalue.text
            if cityname==actualcityname:
                eachcityvalue.click()
                break
        time.sleep(2)

obj=listconcept()
obj.listimplementation("India")
obj.listimplementationcity("Chennai")

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
class dropdown():

    def singleselectdropdown(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        self.driver.maximize_window()
        self.driver.find_element(by=By.CSS_SELECTOR, value="a[data-testid='open-registration-form-button']").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "firstname")))
        self.driver.find_element(by=By.NAME, value="firstname").send_keys("sathish")
        #### clic the dropdown
        daydropdown=Select(self.driver.find_element(by=By.ID, value="day"))
        daydropdown.select_by_index(9)
        monthdropdown = Select(self.driver.find_element(by=By.ID, value="month"))
        monthdropdown.select_by_value("5")
        yeardropdown = Select(self.driver.find_element(by=By.ID, value="year"))
        yeardropdown.select_by_visible_text("2010")

        time.sleep(2)
    def multiselectdropdown(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        self.driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
        self.driver.maximize_window()
        Multiselectdropdown=Select(self.driver.find_element(by=By.XPATH,value="//select[@id='second']"))
        if Multiselectdropdown.is_multiple:
            Multiselectdropdown.select_by_value("burger")
            time.sleep(2)
            Multiselectdropdown.select_by_index(1)
            time.sleep(2)
            Multiselectdropdown.select_by_visible_text("Bonda")
            time.sleep(2)
            Multiselectdropdown.deselect_by_index(3)
            time.sleep(2)
            Multiselectdropdown.deselect_all()


obj=dropdown()
obj.multiselectdropdown()

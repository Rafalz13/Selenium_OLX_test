# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestOlxmotokategorie():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_harmonogram(self):
        self.driver.get("http://ii.up.krakow.pl/")
        harm = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[4]/div[2]/a[1]")
        time.sleep(2)
        harm.click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/h1[1]").text == "STUDIA STACJONARNE I STOPNIA"
        assert self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/div[1]/table/tbody/tr[1]/td[3]").text == "III rok"
        assert self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/div[1]/table/tbody/tr[2]/td[3]/ul/li/span[4]").text == "mgr Imie Nazwisko"
        assert self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/div[1]/table/tbody/tr[2]/td[3]/ul/li/span[2]").text == "21.02.2020"

        assert self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/div[1]/table/tbody/tr[2]/td[3]/ul/li/div/a[2]").text == "Harmonogram"
        self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/div[1]/table/tbody/tr[2]/td[3]/ul/li/div/a[1]").click()


if __name__ == '__main__':
    pytest.main()

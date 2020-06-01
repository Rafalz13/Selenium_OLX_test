
import time
import pytest

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogowanie():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_logowanie0(self):

        self.driver.get("https://www.olx.pl/")
        self.driver.set_window_size(1552, 840)
        ico_log = self.driver.find_element_by_xpath('//*[@id="topLoginLink"]')
        ico_log.click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath("/html/body/div[3]/section/div[3]/div/ul/li[1]/div/form/fieldset/div[1]/div[1]/label").text \
               == "E-mail (do konta OLX)"
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/section/div[3]/div/ul/li[1]/div/form/fieldset/div[2]/div[1]/label").text \
               == "Hasło"
        loguj_button = self.driver.find_element_by_xpath('//*[@id="se_userLogin"]')
        loguj_button.click()
        time.sleep(2)
        # login
        assert  self.driver.find_element_by_xpath('/html/body/div[3]/section/div[3]/div/ul/li[1]/div/form/fieldset/div[1]/div[2]/p/small/div/label').text \
                == 'To pole jest wymagane'
        # hasło
        assert self.driver.find_element_by_xpath(
            '/html/body/div[3]/section/div[3]/div/ul/li[1]/div/form/fieldset/div[2]/div[2]/p/small/div/label').text \
               == 'To pole jest wymagane'

    def test_logowanie1(self):

        self.driver.get("https://www.olx.pl/")
        self.driver.set_window_size(1552, 840)
        ico_log = self.driver.find_element_by_xpath('//*[@id="topLoginLink"]')
        ico_log.click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/section/div[3]/div/ul/li[1]/div/form/fieldset/div[1]/div[1]/label").text \
               == "E-mail (do konta OLX)"
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/section/div[3]/div/ul/li[1]/div/form/fieldset/div[2]/div[1]/label").text \
               == "Hasło"
        log = self.driver.find_element_by_xpath('//*[@id="userEmail"]')
        log.send_keys("login")
        passw = self.driver.find_element_by_xpath('//*[@id="userPass"]')
        passw.send_keys('pass')

        loguj_button = self.driver.find_element_by_xpath('//*[@id="se_userLogin"]')
        loguj_button.click()
        assert self.driver.find_element_by_xpath('/html/body/div[3]/header/div[2]/div/div/div[1]/div[1]/h2').text \
               == 'Twoje ogłoszenia'

class TestOferta():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_oferta0(self):

        self.driver.get("https://www.olx.pl/")
        self.driver.set_window_size(1552, 840)
        time.sleep(1)
        nowa = self.driver.find_element_by_xpath('//*[@id="postNewAdLink"]')
        nowa.click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "/html/body/div[3]/section/div[3]/div/ul/li[1]/div/form/fieldset/div[1]/div[1]/label").text \
               == "E-mail (do konta OLX)"


    def test_oferta1(self):

        self.driver.get("https://www.olx.pl/")
        self.driver.set_window_size(1552, 840)
        time.sleep(1)
        #logowanie
        ico_log = self.driver.find_element_by_xpath('//*[@id="topLoginLink"]')
        ico_log.click()
        time.sleep(2)
        log = self.driver.find_element_by_xpath('//*[@id="userEmail"]')
        log.send_keys('login')
        passw = self.driver.find_element_by_xpath('//*[@id="userPass"]')
        passw.send_keys('passw')
        loguj_button = self.driver.find_element_by_xpath('//*[@id="se_userLogin"]')
        loguj_button.click()

        self.driver.find_element_by_xpath('//*[@id="headerLogo"]').click()
        time.sleep(2)
        nowa = self.driver.find_element_by_xpath('//*[@id="postNewAdLink"]')
        nowa.click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('/html/body/div[3]/section/div/div/form/h1').text \
               == 'Zaczynamy!'


class TestKategorie():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_kategorie_auta(self):
        self.driver.get("https://www.olx.pl/")
        self.driver.set_window_size(1552, 840)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".cat-icon-5").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#bottom5 > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[1]/ul/li[1]/div[2]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[1]/ul/li[1]/div[2]/ul/li[3]/a").click()

    def test_kategorie_moto(self):
        self.driver.get("https://www.olx.pl/")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".cat-icon-5").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#bottom5 > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[1]/ul/li[2]/div[2]/a").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[1]/ul/li[2]/div[2]/ul/li[44]/label[2]").click()
        time.sleep(2)
        

if __name__ == '__main__':
    pytest.main()
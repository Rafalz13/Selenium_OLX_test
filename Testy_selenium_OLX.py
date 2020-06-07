
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
        passw.send_keys('passw')

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

    def test_model_auta(self):
        self.driver.get("https://www.olx.pl/")
        self.driver.set_window_size(1552, 840)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".cat-icon-5").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#bottom5 > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)").click()
        time.sleep(2)
        model = self.driver.find_element_by_xpath(
            "/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[1]/ul/li[1]/div[2]/a")
        model.click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[1]/ul/li[1]/div[2]/ul/li[3]/a").click()
        time.sleep(1)
        assert self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[5]/section/div[1]/div[1]/div[1]/ul/li[4]/h1').text == 'Używane Alfa Romeo sprzedam - OLX.pl'

    def test_model_moto(self):
        self.driver.get("https://www.olx.pl/")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".cat-icon-5").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#bottom5 > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)").click()
        time.sleep(2)
        model = self.driver.find_element_by_xpath(
            "/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[1]/ul/li[2]/div[2]/a")
        model.click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[1]/ul/li[2]/div[2]/ul/li[44]/label[2]").click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[5]/section/div[1]/div[1]/div[1]/ul/li[3]/h1').text \
               == 'Używane motocykle i skutery sprzedam - OLX.pl'

class TestFiltrowanie():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_filtr_polska(self):
        self.driver.get("https://www.olx.pl/")
        self.driver.set_window_size(1552, 840)
        time.sleep(1)
        motoryzacja = self.driver.find_element_by_xpath( "/html/body/div[3]/section[1]/div[1]/div/div[1]/div[1]/div/a/span[2]")
        motoryzacja.click()
        time.sleep(1)
        samochod = self.driver.find_element_by_xpath("/html/body/div[3]/section[1]/div[1]/div/div[2]/ul/li[1]/a")
        samochod.click()
        time.sleep(2)
        #filtry
        kraj_poch = self.driver.find_element_by_xpath('/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[9]/ul/li[2]/div[2]/a')
        kraj_poch.click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[9]/ul/li[2]/div[2]/ul/li[2]/label[2]').click()
        assert self.driver.find_element_by_xpath(
            '/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[9]/ul/li[2]/div[2]/a/span[1]').text == "Polska"

    def test_filtr_cena(self, ):
        self.driver.get("https://www.olx.pl/")
        self.driver.set_window_size(1552, 840)
        time.sleep(1)
        motoryzacja = self.driver.find_element_by_xpath(
                "/html/body/div[3]/section[1]/div[1]/div/div[1]/div[1]/div/a/span[2]")
        motoryzacja.click()
        time.sleep(1)
        samochod = self.driver.find_element_by_xpath("/html/body/div[3]/section[1]/div[1]/div/div[2]/ul/li[1]/a")
        samochod.click()
        time.sleep(2)
        cena_min = self.driver.find_element_by_xpath(
            '/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[2]/ul/li/div[2]/div[1]/a/span[1]')
        cena_min.click()
        self.driver.find_element_by_css_selector('ul.binded:nth-child(3) > li:nth-child(4) > a:nth-child(1)').click()
        time.sleep(1)
        cena_max = self.driver.find_element_by_xpath(
            '/html/body/div[3]/header/div[2]/div/form/noindex/div/fieldset[2]/ul/li[2]/ul/li/div[2]/div[2]/a/span[1]')
        cena_max.click()
        self.driver.find_element_by_css_selector('ul.binded:nth-child(3) > li:nth-child(10) > a:nth-child(1)').click()
        time.sleep(1)
        sort = self.driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[1]/div/div[1]/form/dl/dt/a')
        sort.click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[1]/div/div[1]/form/dl/dd/ul/li[3]/a').click()
        time.sleep(2)
        cena_samoch = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[5]/section/div[3]/div/div[1]/table[1]/tbody/tr[3]/td/div/table/tbody/tr[1]/td[3]/div/p/strong').text
        cena_samoch = cena_samoch[0:2]
        assert int(cena_samoch) >32
        

if __name__ == '__main__':
    pytest.main()
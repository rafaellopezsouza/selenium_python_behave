from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from features.support.Browser import Browser
from features.utils import logger, constants
from features.utils import global_variables as gv


class TestesArquiteturaProjeto(object):
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def __get_browser(self):
        browser = Browser(gv.browser)
        return browser.select_browser()

    def __get_elements(self):
        self.elemento_pesquisa = self.driver.find_element(By.NAME, 'q')

    def acessar_pagina(self):
        # self.driver = self.__get_browser()
        self.__get_elements()
        try:
            logger.logging.info(constants.ACESSANDO_URL % self.url)
            self.driver.get(self.url)
        except Exception as e:
            logger.logging.error(constants.ERRO_ACESSAR_URL % self.url % e)

    def clicar_campo_pesquisa(self, campo):
        try:
            logger.logging.info(constants.CLICANDO_CAMPO % campo)
            self.elemento_pesquisa.click()
        except Exception as e:
            logger.logging.error(constants.ERRO_CLICAR_CAMPO % campo % e)

    def realizar_pesquisa(self, texto):
        try:
            logger.logging.info(constants.TEXTO_CAMPO % texto)
            self.elemento_pesquisa.sendKeys(str(texto) + Keys.ENTER)
        except Exception as e:
            logger.logging.error(constants.ERRO_CLICAR_CAMPO % texto % e)

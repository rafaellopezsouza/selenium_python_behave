from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from features.utils import constants, logger


class Browser(object):
    def __init__(self, browser='chrome', headless=False, maximized=True):
        self.browser = browser
        self.headless = headless
        self.maximized = maximized

    def select_browser(self):
        try:
            match self.browser:
                case 'chrome':
                    from selenium.webdriver.chrome.options import Options
                    options = Options()
                    if self.headless:
                        options.add_argument("--headless")
                    elif self.maximized:
                        options.add_argument("--start-maximized")
                    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                case 'chromium':
                    browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
                case 'firefox':
                    from selenium.webdriver.firefox.options import Options
                    options = Options()
                    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
                case 'ie':
                    browser = webdriver.Ie(IEDriverManager().install())
                case 'edge':
                    browser = webdriver.Edge(EdgeChromiumDriverManager().install())
                case 'opera':
                    browser = webdriver.Opera(executable_path=OperaDriverManager().install())
                case _:
                    logger.logging.info(constants.NAVEGADOR_NAO_ENCONTRADO % self.browser)
                    return None

            logger.logging.info(constants.NAVEGADOR_ENCONTRADO % self.browser.upper())
            return browser
        except Exception as e:
            logger.logging.error(constants.ERRO_CAPTURADO % e)
            raise

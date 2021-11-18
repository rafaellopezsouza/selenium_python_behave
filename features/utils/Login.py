from features.utils import global_variables as gv, logger, constants


class Login(object):
    def __init__(self, url=None):
        self.driver = gv.driver
        self.url = url

    def login_com_sucesso(self):
        try:
            logger.logging.info(constants.ACESSANDO_URL % self.url)
            self.driver.get(self.url)
        except Exception as e:
            logger.logging.error(constants.ERRO_ACESSAR_URL % self.url, e)

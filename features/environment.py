from features.support.Browser import Browser
from features.utils import global_variables as gv, logger, constants
from features.support.enviroments.SetEnvironments import SetEnvironments


def before_all(context):
    logger.logging.info(logger.LAYOUT_LOGS)
    logger.logging.info(constants.INICIANDO_CENARIO_TESTE)
    gv.env = context.config.userdata['env'].upper()
    SetEnvironments(gv.env)
    logger.logging.info(constants.AMBIENTE_EXECUCAO % gv.env)
    gv.browser = context.config.userdata['nav']
    gv.driver = Browser(gv.browser).select_browser()


def after_all(context):
    logger.logging.info(constants.FECHANDO_NAVEGADOR)
    logger.logging.info(constants.FINALIZADO_CENARIO_TESTE)
    logger.logging.info(logger.LAYOUT_LOGS)
    gv.driver.quit()

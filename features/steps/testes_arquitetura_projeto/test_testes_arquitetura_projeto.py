from behave import when, then
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from features.utils import global_variables as gv, logger, constants


@when(u'abrir o site do google')
def abrir_site_google(context):
    url = 'https://google.com.br'
    gv.driver.get(url)


@when(u'faça uma pesquisa "{texto_pesquisa}"')
def fazer_uma_pesquisa(context, texto_pesquisa):
    context.texto_pesquisa = texto_pesquisa
    element = gv.driver.find_element(By.NAME, "q")
    element.click()
    element.send_keys(context.texto_pesquisa + Keys.ENTER)


@then(u'a pesquisa deve ser exibida')
def exibir_pesquisa(context):
    titulo_pesquisa = f'{context.texto_pesquisa} - Pesquisa Google'
    try:
        assert gv.driver.title == titulo_pesquisa
        logger.logging.info(constants.PASSO_EXECUTADO_SUCESSO)
    except Exception:
        logger.logging.error(constants.MSG_ERRO_COMPARACAO % (gv.driver.title, titulo_pesquisa))
        raise

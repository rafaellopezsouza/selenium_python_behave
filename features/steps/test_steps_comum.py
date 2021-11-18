from behave import given
from features.utils.Login import Login
from features.utils import global_variables as gv


@given(u'que esteja logado com o usuário "{type_user}"')
def login(context, type_user):
    match type_user:
        case 'padrão':
            Login(gv.url_gestor).login_com_sucesso()
        case 'qualquer':
            pass

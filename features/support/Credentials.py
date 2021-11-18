class Credentials(object):
    def __init__(self):
        self.user_default = "testes_arquitetura_projeto-adm"
        # self.user_pontal = "pontal"
        # self.user_scob = "testes_arquitetura_projeto-escob1@testes_arquitetura_projeto.com"
        self.password_default = "q1w2e3"

    def get_user_default(self):
        return self.user_default

    def get_password(self):
        return self.password_default

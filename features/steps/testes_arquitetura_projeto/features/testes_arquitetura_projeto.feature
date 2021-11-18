#language: pt

@all @testes_arquitetura_projeto @login_steps_comum
Funcionalidade: Realizar a inclusão de um número de boleto, na Lista Restrita Boletos
  @wip
  Cenario: Deletar a regra inserida
#    Dado que esteja logado com o usuário "padrão"
    Dado que esteja logado com o usuário "qualquer"
    Quando abrir o site do google
    E faça uma pesquisa "pontalTech"
    Então a pesquisa deve ser exibida
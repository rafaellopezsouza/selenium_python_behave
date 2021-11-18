# Testes Automatizados de E2E utilizando BDD

## Descrição

- **Inicio:** 16/11/2021
- **Objetivo:** Este projeto é para implementar testes automatizados, utilizando a linguagem de programação
  Python/Selenium.
- **Cenários de Testes:** A escrita dos testes será no formato Gherkin, utilizando o BDD para a maior clareza e
  entendimento dos testes. Os BDDs poderão ser reutilizados em outros projetos e/ou mudanças de linguagem/framework caso
  seja necessário.

## Como Instalar:

### Pré-requisitos:

- [Python 3.10 ou superior](https://www.python.org/downloads/)
- [Behave](https://behave.readthedocs.io/en/latest/)
- [Git](https://git-scm.com/)
- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/)

### Importar o projeto

- Abra o Pycharm ou outro Editor/IDE de sua preferência, crie um diretório local.
- Acesse o diretório pelo terminal da máquina ou do Pycharm.
- Execute o comando: **git init**
- Após realize o clone do projeto: **git clone url_do_projeto**
- Instale as [bibliotecas](#instalao-das-bibliotecas) utilizados no projeto, e aponte o Pycharm para o interpretador do
  python instalado nos pré-requisitos.

### Instalação das bibliotecas:

Abra o terminal, da máquina, ou da IDE dentro do projeto, e digite os comandos abaixo:

    pip install -r requirements.txt

### Instalação do webdriver

Instalar a biblioteca manager-webdriver, que gerencia o webdriver, sem a necessidade de instalar manualmente cada
webdriver de acordo com o seu navegador.

    pip install webdriver-manager

## Boas práticas

### Para criar os testes

**1**. Os casos de testes devem estar devidamente identados. No Pycharm, use o atalho "CTRL+L" para identar
corretamente.

    Cenário: Escreva o titulo do cenário
        Dado que um usuário esteja autenticado com sucesso
        Quando clicar no botão "Criar"
        Então a funcionalidade deve ser criada com sucesso

**2**. Quando estiver desenvolvendo o código de uma feature nova, use uma tag temporária **@wip** (WorkInProgress), pois
facilitará outro QA a identificação de que essa feature é temporária. Esta tag deve ser removida ou substituída pela
definitiva ao fazer abrir um PR (Pull Request). Siga a padronização de tags descrita [aqui](#padronizao-de-tags)

**3**. A arquitetura do projeto deve seguir alguams boas práticas de programação.

- O Projeto terá a pasta raiz, seguida do diretório com o nome de cada produto.
- Dentro desse diretório, abrirá mais dois diretórios, um de **feature** e outro de **functions**.
- Dentro da **"features"**, deve-se ter quantos diretórios se achar necessário, de acordo com a necessidade. As features
  é onde estará a escrita na linguagem Gherkin (BDD).
- Dentro da **"functions"**, deve ter a lógica para a execução dos testes.
- Dentro de cada **"produto"**, haverá os arquivos de execução dos testes relativos ao produto. Sempre começando com "**
  test_**". seguido do produto, funcionalidade. Ex: "**test_gestor_realizar_login.py**"

**4**. Após escrever os cenários no arquivo _.feature_, execute o comando para gerar os snippets do teste criado:

    behave --tags=@wip

**5**. Após executar o passo 4, os testes do cenário será executado, e exibirá os "snippets" gerado no console do
Pycharm. Esses snippets deverão ser salvos dentro do arquivo iniciado com "test_" relacionado a sua feature que foi
desenvolvida anteriormente.

     You can implement step definitions for undefined steps with these snippets:

     @given(u'que um usuário esteja autenticado com sucesso')
     def step_impl(context):
     raise NotImplementedError(u'STEP: Given que um usuário insira um CPF válido e existente')

### Padronização de tags

- No processo de de desenvolvimento deve-se usar **@wip**
- Quando uma feature tem um bug, deve-se usar a tag **@bug**. Quando somente uma linha do BDD está com Bug, deve-se
  colocar a tag acima da linha com bug, e comentar somente a linha com com bug usando o **#** no incio da frase.
- Quando uma feature não está conluída, deve-se usar a tag **@todo**
- **TODAS** as funcionalidades devem iniciar com **@all**:
    - Seguido da tag com o nome do **produto**. Ex. **@gestor**
    - Seguido com a tag do nome **funcionalidade**: Ex. **@login**
- **Exemplo:** @all @produto @funcionalidade

### Executar os testes do projeto:

Todos os testes iniciará com _behave_. Pode-se incluir quantas opções desejar, separando as palavras com espaço.

1. Executar testes sem gerar relatório HTML.
    - Executar todos os testes:
        - behave -- ou behave -t@all
    - Executar algum produto ou conjunto de funcionalidades:
        - behave -t@nome_tag
    - Executar testes exibindo apenas um resumo no comsole:
        - behave --format=progress -t@nome_tag
    - Deixar de executar alguma tag especifica:
        - behave -t~@nome_tag
    - Executar testes em um ambiente especifico:
        - behave -D env=nome_ambiente
    - Executar várias tags de uma vez. Neste exemplo abaixo, irei executar todos os testes no ambiente de homolog, menos
      as tags _bug_ e _todo_, e exibindo somente um resumo de cada teste:
        - behave -D env=hmg --format=progress --tags=@all --tags=~@bug --tags=~@todo
2. Executar testes gerando relatório HTML:
    - Gerar arquivos .json na pasta reports. Neste caso, não utilizaremos o behave, e sim o allure para gerar os
      relatórios em HTML:
        - behave --tags=@nome_tag -f allure_behave.formatter:AllureFormatter -o reports ./features
    - Exibir o relatório gerado no passo anterior:
        - allure serve reports/

No Windows o allure pode apresentar problemas na exibição do relatório em HTML. Documentação completa [AQUI.](https://docs.qameta.io/allure/) Caso isso aconteça, abra o terminal do "
Windows PowerShell" e execute os comandos abaixo:

    Set-ExecutionPolicy RemoteSigned -scope CurrentUser

    Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
    
    scoop install allure

Após executar os comandos acima, vá para o diretório do projeto pelo terminal do PowerShell, ou reinicie o Pycharm, e
execute o comando para exibir o relatório.

    allure serve reports/

### Boas práticas de desenvolvimento

Além das boas praticas na [padronização das tags](#padronizao-de-tags), temos algumas outras boas práticas a serem
feitos no código.

- Usar **#TODO** quando um método/função não está concluída, ou precisa ser refatorada.
- Usar DocStrings para fazer comentários do seu código quando necessário, logo abaixo do nome da função/método, insira o
  docStrings. Ex: **"""Insira seu comentário aqui"""**
- Quando parte do seu código não deve ser executada, deve-se usar o # antes de cada linha para ser ignorada no momento
  da execução. Ex: **# ignorar_essa_parte_do_codigo**
- Nome das variaveis/métodos/funções deve-se seguir o padrão snake_case. Sendo todas as letras em "lower_case",
  separadas por underscore, quando nome composto. Ex: **nome_de_uma_variavel_ou_metodo**
- Nome das classes, deve seguir o padrão CamelCase, sendo a primeira letra de cada palavra em "UpperCase". Ex: **
  NomeDeUmaClasse**
- Nome das variáveis globais, devem seguir no padrão UPPERCASE. Ex: **NOME_DE_UMA_VARIAVEL_GLOBAL**
- Dê nome objetivo e direto a suas variáveis/funções/métodos. Ex: variável com o nome do usuário, **usuario=None**:
- Ao iniciar uma nova feature, crie uma nova branch de desenvolvimento a partir da master.
- Ao concluir uma nova feature, faça um merge da master para o seu projeto, somente depois suba o PR. Isso evitará
  conflitos no momento do merge da sua branch para a master.
- Dica: Assim que concluir um cenário/feature do teste, faça o commit e push para a remote/branch, pois se caso sua
  máquina der algum problema, não perderá o que fez.




# login_python_selenium
Script básico de login via selenium

## Pré requisitos:
- Python instalado;
- pip instalado;
- Download do Chromedriver (webdriver) na pasta c:/opt/webdriver;

## Criar pasta de projeto;
- instalar o virtualenv
- iniciar o virtualenv com o comando: "virtualenv env"
- instalar selenium via pip "pip install selenium" (Esta é a lib para automação);
- instalar behave via pip "pip install behave" (Esta é a lib para BDD - https://medium.com/iclinic/princ%C3%ADpios-de-bdd-com-python-behave-e-selenium-b3bbe0d4fa47);
- criar arquivo de BDD, cada linha corresponde a um comando no arquivo python de automacao. 
ex:

Arquivo do behave ex:<<funcionalidade>>.feature
```
#language: pt
Funcionalidade: Logar na rede social Facebook
   
   '''Eu como usuario quero acessar a pagina inicial do facebook com dados de login.'''

   Cenario: Me logar na rede social Facebook
   Dado acesso a pagina de login do face
   Quando preencho minha senha e usuário
   Então termino
```

- Dado (palavra reservada) tem que ter o msm conteudo na anotaçcao > @given do projeto.py
- Quando(palavra reservada, se tiver mais um quando, iniciar a segunda linha com 'E') tem que ter o msm conteudo na anotaçcao > @when do projeto.py
- Entao(palavra reservada) tem que ter o msm conteudo na anotaçcao > @then do projeto.py

- Seta a url a ser acessada;
- Setar os valores nos campos, para acessar os campos seguir o manual do selenium:
https://selenium-python.readthedocs.io/locating-elements.html
- finaliza o projeto.

import time
from behave import given, when, then

# Variável com a URL do site que iremos interagir.
base_url = 'https://www.facebook.com'

# Variáveis com os elementos que iremos interagir na página
button_login = '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button'
username='seuemail'
password='suasenha'

@given(u'acesso a pagina de login do face')
def step_impl(context):
    context.web.get(base_url)

@when(u'preencho minha senha e usuário')
def step_log(context):
    username_input=context.web.find_element_by_id("email")
    password_input=context.web.find_element_by_id("pass")
    username_input.send_keys(username)
    password_input.send_keys(password)

    btn_login=context.web.find_element_by_xpath(button_login)
    btn_login.click()

@then(u'termino')
def step_impl(context):
    time.sleep(30) #sleep for 30 secs
    print('Feito')
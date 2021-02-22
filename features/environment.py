from selenium import webdriver


def before_all(context):
    context.web=webdriver.Chrome("/opt/chromedriver/chromedriver.exe")

def after_step(context,step):
    print()

def after_all(context):
    context.web.quit()    
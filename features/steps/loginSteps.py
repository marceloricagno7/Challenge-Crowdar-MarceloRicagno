import time

from behave import given, when, then
from lib.pages.loginPage import LoginPage

@given('Ingresamos a la web')
def step_impl(context):
    driver = context.driver
    loginPage = LoginPage(driver)

    # Nos dirigimos a la URL de la web
    context.driver.get(context.URL_BASE_WEB)

@when('iniciamos sesion en la pagina con el usuario "{user}"')
def step_impl(context, user):
    driver = context.driver
    loginPage = LoginPage(driver)

    # Setiamos el Context del User dependiendo de cual se quiera usar y logeamos
    if user == 'Marcelo':
        loginPage.send_login(context.USER_FAIL, context.PASSWORD_CORRECT)
    elif user == 'Standard':
        loginPage.send_login(context.USER_STANDARD, context.PASSWORD_CORRECT)
    else:
        print("El usuario que elegio no existe en los registros")
    time.sleep(2)

@then('Verificamos que el login sea "{status}"')
def step_impl(context, status):
    driver = context.driver
    loginPage = LoginPage(driver)

    # Verificamos que tipo de Status es para realizar las verificaciones correspondientes
    if status == 'Fallido':
        text_error = loginPage.verify_error_message()
        #Se hace que falle esta verificacion para que salga como error y haga captura
        assert text_error == 'Epic sadface: Username and password do not match any user in this service.', \
            'El mensaje de error capturado es distinto al mensaje de comparacion'
    elif status == 'Exitoso':
        text_menu = loginPage.get_text_menu()
        assert text_menu == 'Products'
    else:
        print("El Status ingresado no es correcto")

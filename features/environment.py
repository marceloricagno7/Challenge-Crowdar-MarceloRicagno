import glob
import os
import json
import allure

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from behave.model_core import Status

global stepPass
global stepFail


# Se ejecuta antes de cada escenario
def before_scenario(context, scenario):
    if context.config.userdata["ENV"] == "TEST":
        # Setiamos variables que nos seran de utilidad en los Test
        with open('environments/TEST.json') as f:
            environment = json.load(f)
        context.ML_DEPARTMENTS_API = environment["ml_departments_api"]
        context.URL_BASE_WEB = environment["base_url_web"]
        context.USER_FAIL = environment['USER_FAIL']
        context.USER_STANDARD = environment['USER_STANDARD']
        context.PASSWORD_CORRECT = environment['PASSWORD_CORRECT']

    # Configurar si debe ejecutarse en modo headless. Por defecto: False.
    headless = context.config.userdata.get("HEADLESS", "FALSE").upper() == "TRUE"

    # Setiamos las configuraciones del Chrome Profile para el Driver
    if context.config.userdata["NAVEGADOR"] == "CHROME":
        chrome_profile = Options()
        chrome_profile.add_argument('--incognito')
        chrome_profile.add_argument('--allow-running-insecure-content')
        chrome_profile.add_argument('--ignore-certificate-errors')
        chrome_profile.add_argument("--disable-application-cache")
        chrome_profile.add_argument('--lang=es')
        chrome_profile.add_experimental_option('prefs', {'intl.accept_languages': 'es_ES',
                                                         'profile.managed_default_content_settings.images': 2})
        chrome_profile.add_argument("--start-maximized")
        chrome_profile.add_argument("--disable-features=VizDisplayCompositor")

        # Si el modo headless es TRUE se agrega esta config
        if headless:
            chrome_profile.add_argument("--headless")
            chrome_profile.add_argument("--disable-gpu")  # Recomendado para ciertas configuraciones gráficas
            chrome_profile.add_argument("--window-size=1920,1080")

        # Configuramos e inicializamos el Chrome Driver
        chrome_path = ChromeDriverManager().install()
        context.driver = webdriver.Chrome(service=webdriver.chrome.service.Service(chrome_path),
                                        options=chrome_profile)

    # Setiamos las configuraciones del Firefox Profile para el Driver en caso que se quiera usar este
    elif context.config.userdata["NAVEGADOR"] == "FIREFOX":
        firefox_profile = FirefoxOptions()
        firefox_profile.add_argument('--incognito')  # Private mode
        firefox_profile.add_argument('--ignore-certificate-errors')
        firefox_profile.set_preference('intl.accept_languages', 'es-ES')  # Idioma en español
        firefox_profile.set_preference('permissions.default.image', 2)  # No cargar imágenes
        firefox_profile.add_argument("--start-maximized")

        # Si el modo headless es TRUE se agrega esta config
        if headless:
            firefox_profile.add_argument("--headless")
            firefox_profile.add_argument("--window-size=1920,1080")

        # Configuramos e inicializamos el Gecko Driver
        firefox_path = GeckoDriverManager().install()
        context.driver = webdriver.Firefox(service=webdriver.firefox.service.Service(firefox_path),
                                           options=firefox_profile)

    else:
        raise ValueError("Navegador no soportado. Usa 'CHROME' o 'FIREFOX'.")


    # En todos los proyectos suelo abrir la URL desde esta instancia, a modo visible para que no quede raro el
    # escenario en Gherkin sin el Given lo abrire desde los Steps

    # Nos dirigimos a la URL de la web
    #context.driver.get(context.URL_BASE_WEB)


def after_scenario(context, scenario):
    global stepFail, stepPass
    f = open('./Logs/' + context.nomArchivo, 'a')

    espacios = 94 - len(scenario.name)
    if scenario.status == Status.failed:
        f.write('\n' "SCENARIO>  {:<10}".format(scenario.name) + '0      1'.rjust(espacios))
        f.close()
        stepFail += 1

    if scenario.status == Status.passed:
        f.write('\n' "SCENARIO>  {:<10}".format(scenario.name) + '1      0'.rjust(espacios))
        f.close()
        stepPass += 1

    # Cerramos la pestania una vez que se termina de correr el caso
    context.driver.quit()


def before_all(context):
    # Verificamos si la carpeta Allure results existe, en caso que si se eliminan los archivos adentro asi no
    # almacenamos datos innecesarios en el repo de cada run
    if os.path.exists('allure-results'):
        for file in os.listdir('allure-results'):
            file_path = os.path.join('allure-results', file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("Carpeta allure-results Limpia.")
    else:
        print("Todo en condiciones para ejecutar el los casos")

    global stepFail, stepPass
    stepFail = 0
    stepPass = 0
    files = glob.glob('./Logs/*')
    for f in files: os.remove(f)
    # fecha = datetime.now()
    # fechaHora = fecha.strftime("%d-%m-%Y %H%M%S")
    f = open('./Logs/Logs Status.txt', 'w')
    context.nomArchivo = 'Logs Status.txt'
    f.write(
        'TABLE>          NOMBRE TC                                                                      PASS   FAIL')

def after_step(context,step):
    if step.status=='failed':
        # Almacenamos temporalmente la captura de pantalla y lo leemos para disponibilizarlo en Reportes de , al ultimo
        # limpiamos el archivo
        screenshot_path = "temp_failed_step.png"
        if hasattr(context, "driver"):  # Asegúrate de que `context.driver` sea un objeto Selenium WebDriver
            context.driver.save_screenshot(screenshot_path)
            with open(screenshot_path, "rb") as file:
                screenshot_bytes = file.read()
            allure.attach(screenshot_bytes, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            os.remove(screenshot_path)

def after_all(context):
    global stepFail, stepPass
    f = open('./Logs/' + context.nomArchivo, 'a')
    f.write('\n' "RESULTS>  TC PASADOS: " + str(stepPass) + "    TC FALLADOS: " + str(stepFail) + "    TC TOTALES: " + str(
        stepPass + stepFail))

    try:
        with open("./Logs/Logs Status.txt", "r") as archivo:
            for linea in archivo:
                print(linea.rstrip())
    except Exception as error:
        print('Error al leer archivo log ' + error)

    print("RESULTS>  RESUME   TC PASADOS: " + str(stepPass) + "    TC FALLADOS: " + str(
        stepFail) + "    TC TOTALES: " + str(
        stepPass + stepFail))

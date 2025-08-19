<h1 align="center">✨  CHALLENGE CROWDAR - MARCELO RICAGNO   ✨</h1>
Este proyecto contiene la realizacion del challenge para Crowdar

# Índice

* [Requisitos necesarios](#Requisitos-necesarios)
* [Ejecución de tests](#Ejecución-de-tests)
* [Reportes](#reportes)

## Requisitos necesarios

### Python 
Versión utilizada 3.13



### Repositorio 

Clonar Repositorio [Challenge Crowdar - Marcelo Ricagno](https://github.com/marceloricagno7/Challenge-Crowdar-MarceloRicagno.git)


### Pycharm
Idle utilizado para el desarrollo del proyecto

### Venv
Creamos el virtual enviroment para la ejecucion local con lo siguientes comandos:

`python -m venv env`

### Requirements

Intalamos las librerias y dependencias del proyecto las cuales se ubican en el archivo requirements.txt, 
para ello se debe ejecutar el siguiente comando dentro de la raiz del proyecto:

`./env/Scripts/activate`

y luego el siguiente comando:

`pip install -r requirements.txt`

### Environments

Sera necesario que peguen el archivo TEST.json dentro de la carpeta */environments*, ya que este archivo contiene las URL y las
credenciales de acceso de los usuarios.Este archivo no se sube al repositorio ya que esta contemplado por el .gitignore al ser
un json con informacion sensible. El mismo sera enviado junto con la documentacion en el mail.

## Ejecución de tests

Ejecutar los test indicados por el challenge, bajo el tag *@challengeTest*, navegador Chrome:

Modo NO-HEADLESS >
`behave --tags challengeTest ./features -D ENV=TEST -D NAVEGADOR=CHROME`

Modo HEADLESS >
`behave --tags challengeTest ./features -D ENV=TEST -D NAVEGADOR=CHROME -D HEADLESS=TRUE`

Ejecutar los test indicados por el challenge, bajo el tag *@challengeTest*, navegador Firefox:

Modo NO-HEADLESS >
`behave --tags challengeTest ./features -D ENV=TEST -D NAVEGADOR=FIREFOX`

Modo HEADLESS >
`behave --tags challengeTest ./features -D ENV=TEST -D NAVEGADOR=FIREFOX -D HEADLESS=TRUE`

En caso de correr algun test con ulgun otro TAG de los disponibles en el *.feature* se modifica en el script la parte "*--tags {InsertarTagDeseado}*"

## Reportes

Para revisar el reporte Generado por allure, solo basta con ejecutar el siguiente comando y se le abrira una web con el reporte:

`allure serve`

Alli adentro se podran ver todos los steps ejecutados de cada caso, y en los steps donde haya ocurrido algun error se encontrara 
descripcion del mismo y la captura de pantalla de la web

Ademas del reporte, el proyecto genera un archivo Logs para ver de forma sencilla en TXT, cual caso paso y cual no con un resumen de casos exitos y fallidos.
Esto es muy util cuando integramos el proyecto en CI/CD ya que aveces se necesita un resumen en un TXT para analizar el passrate

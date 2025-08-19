Feature: Challenge Testing WEB

  Background:
    Given Ingresamos a la web

  @challengeTest @fail
  Scenario: Inicio sesion Fallido con username incorrecto y clave correcta
    When iniciamos sesion en la pagina con el usuario "Marcelo"
    Then Verificamos que el login sea "Fallido"

  @challengeTest @success
  Scenario: Agregar al carrito desde la ficha de detalle del producto
    When iniciamos sesion en la pagina con el usuario "Standard"
    Then Verificamos que el login sea "Exitoso"
    When Seleccionamos el producto "Sauce Labs Backpack" y lo agregamos al carrito
    Then Verificamos que el producto se encuentra en el carrito
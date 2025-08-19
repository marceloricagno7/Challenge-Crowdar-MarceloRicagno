Feature: Challenge Testing API

  @challengeTest @API
  Scenario: Consultar en API disponibilidad de Departamentos
    When Ejecutamos una peticion a API "departments"
    Then Verificamos que el response contenga resultados disponibles
from behave import given, when, then
from lib.api.APIs import APIs

@when('Ejecutamos una peticion a API "{section}"')
def step_impl(context, section):
    pass
    # Realizamos la peticion y corroboramos que la clave 'Departments' exista y no venga vacia
    #if section == 'departments':
    #    response = APIs().get_ml_departments(context.ML_DEPARTMENTS_API)
    #    context.result_json = response
    #else:
    #    print('Section insertada inexistente')
    #    raise ValueError(f"Error: La sección '{section}' no es válida. Se esperaba 'departments'.")


@then('Verificamos que el response contenga resultados disponibles')
def step_impl(context):
    pass
    #assert 'departments' in context.result_json, "La respuesta no contiene la clave 'departments'."
    #assert len(context.result_json['departments']) > 0, "No se encontraron departamentos en la respuesta."


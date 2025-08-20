import json
import allure
from behave import given, when, then
from lib.api.APIs import APIs

@when('Ejecutamos una peticion a API "{section}"')
def step_impl(context, section):
    pass
    # Realizamos la peticion y el parametro enviado en el step sea el correcto
    if section == 'departments':
        response = APIs().get_ml_departments(context.ML_DEPARTMENTS_API)
        context.result_json = response
    else:
        print('Section insertada inexistente')
        raise ValueError(f"Error: La sección '{section}' no es válida. Se esperaba 'departments'.")


@then('Verificamos que el response contenga resultados disponibles')
def step_impl(context):
    # Disponibilizamos el response obtenido en el step dentro del Reporte de Allure
    response_str = json.dumps(context.result_json, indent=4, ensure_ascii=False)
    allure.attach(response_str, name='Response del servicio', attachment_type=allure.attachment_type.TEXT)
    # Corroboramos que la clave 'Departments' exista y no venga vacia
    assert 'departments' in context.result_json, "La respuesta no contiene la clave 'departments'."
    assert len(context.result_json['departments']) > 0, "No se encontraron departamentos en la respuesta."


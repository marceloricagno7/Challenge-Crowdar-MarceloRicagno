import json

import requests
from hamcrest import assert_that, equal_to

class basePageApi():
    _intance = None

    # Se valida si existe una instancia de la clase, si no existe la crea
    def __new__(cls, *args, **kwargs):
        if not cls._intance:
            cls._intance = object.__new__(cls)
        return cls._intance

    def API_GET(self, url, params):
        try:
            response = requests.get(url=url, params=params, timeout=10)
            result_json = json.loads(response.text)
            return result_json
        except Exception as error:
            assert_that(False, equal_to(True),
                        reason="Error al intentar realizar la peticion GET. Error:" + str(error))
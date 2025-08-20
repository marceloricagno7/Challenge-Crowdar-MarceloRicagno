from lib.api.basePageApi import basePageApi

class APIs(basePageApi):
    _intance = None
    def __new__(cls, *args, **kwargs):
        if not cls._intance:
            cls._intance = object.__new__(cls)
        return cls._intance

    # Se valida si existe una instancia de la clase, si no existe la crea

    def get_ml_departments(self, url, params=None):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }
        return self.API_GET(url, params, headers=headers)


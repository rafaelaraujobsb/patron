import requests
from loguru import logger

from patron.config import KEY_DOLLAR

class ApiDolar:
    URL = 'http://apilayer.net/api/live'

    @staticmethod
    def get():
        logger.info('[+] REQUISICAO API DOLAR')   

        params = {'access_key': KEY_DOLLAR, 'currencies': 'USD, BRL'}

        return requests.get(ApiDolar.URL, params=params).json()    

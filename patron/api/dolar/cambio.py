from datetime import datetime

from flask import request
from loguru import logger
from flasgger import swag_from
from flask_restful import Resource

from patron.servico.request import ApiDolar
from patron.api.resposta_api import Resposta
from patron.servico.database import Database


class RotinaDolar(Resource):

    @swag_from('../../../docs/api/rotina_get.yml')
    def get(self):
        if datetime.now().strftime('%A') not in {'Sunday', 'Saturday'}:
            resultado = ApiDolar.get()

            if resultado['success']:
                json = {
                    'timestamp': resultado['timestamp'],
                    'cotacao': resultado['quotes']['USDBRL']
                }

                Database().set_document('dolar', json.copy())
                logger.info('[+] COTACAO SALVA')

                return Resposta.retorno(json)
            else:
                logger.info('[-] REQUISICAO API DOLAR PROBLEMA')
                return Resposta.error('Problema com a API Dólar!')
        else:
            logger.info('[-] REQUISICAO API DOLAR INVALIDO')
            return Resposta.nao_aceito('A API Dólar não pode ser requisitada!')


class CambioDolar(Resource):

    @swag_from('../../../docs/api/cambio_post.yml')
    def post(self):
        json = request.json

        if all(map(json.get, ['de', 'para', 'valor'])):
            logger.info('[+] FAZER CAMBIO')
            
            resultado = Database().get_document('dolar', visible={'_id': 0}, sort=[('timestamp', -1)], max=1)[0]
            valor_dolar = resultado['cotacao']

            if json['de'] == 'BRL':
                return Resposta.retorno({'conversao': json['valor']/valor_dolar})
            else:
                return Resposta.retorno({'conversao': json['valor']*valor_dolar})
        else:
            logger.info('[-] JSON INVALIDO')            
            return Resposta.error('JSON inválido!')

from datetime import datetime

from flask import request
from loguru import logger
from flasgger import swag_from
from flask_restful import Resource

from patron.api.resposta_api import Resposta
from patron.servico.database import Database


class ListarProduto(Resource):
    """Listar os produtos"""


class Produto(Resource):

    @swag_from('../../../docs/api/produto_post.yml')
    def post(self):
        json = request.json

        if all(map(json.get, ['valor', 'qtd', 'ctg', 'site', 'modelo', 'mtd_pg'])):
            logger.info('[+] CADASTRAR PRODUTO')

            json['_id'] = json.pop('modelo')
            Database().set_document('produto', json)

            return Resposta.sucesso('Produto cadastrado!')
        else:
            logger.info('[-] JSON INVALIDO')            
            return Resposta.error('JSON inválido!')

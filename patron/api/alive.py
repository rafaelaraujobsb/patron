from flasgger import swag_from
from flask_restful import Resource
from pymongo.errors import ServerSelectionTimeoutError

from patron.api.resposta_api import Resposta
from patron.servico.database import Database


class Alive(Resource):

    @swag_from('../../docs/api/alive_get.yml')
    def get(self):
        try:
            Database().get_names_collections()
        except ServerSelectionTimeoutError:
            return Resposta.error('Mongo fora do ar!')

        return Resposta.sucesso('API ON!')

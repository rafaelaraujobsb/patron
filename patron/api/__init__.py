from flask import Blueprint
from flask_restful import Api

from patron.api.alive import Alive
from patron.api.produto.compra import ListarProduto, Produto
from patron.api.dolar.cambio import RotinaDolar, CambioDolar


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Alive, '/alive')

api.add_resource(CambioDolar, '/dolar')
api.add_resource(Produto, '/cadastrar/produto')


# Rotina
api.add_resource(RotinaDolar, '/dolar/atualizar')


from flask import Flask
from loguru import logger
from flasgger import Swagger

from patron.api import api_bp


logger.add("api.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", rotation="500 MB")

template = {
    "swagger": "2.0",
    "info": {
        "title": "PATRON",
        "description": "",
        "version": "0.0.1"
    },
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ]
}

app = Flask(__name__)
swagger = Swagger(app, template=template)

app.register_blueprint(api_bp, url_prefix='/api')

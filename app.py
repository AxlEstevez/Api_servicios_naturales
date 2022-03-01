from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from resources.routers import initRouter

app = Flask(__name__)
cors = CORS(app)
api = Api(app)
jwt = JWTManager(app)

initRouter(api)

if __name__ == '__main__':
    app.run(debug=True)
import json
from flask_restful import Resource
import requests


class GetDataAire(Resource):
    def get(self):
        api_url = "https://api.datos.gob.mx/v2/sinaica"

        try:
            response = requests.get(api_url)
            json_response = json.loads(response.text)
            json_data = json_response["results"]
            return(json_data, 200)
        except Exception as e:
            print(e)
            return(
                {
                "Descripcion": "Ha ocurrido un error al solicitar los datos"
                },
                500
            )

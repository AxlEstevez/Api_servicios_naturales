import urllib3
import io
import gzip
import json
from flask import Response, request
from flask_restful import Resource


class GetDataFromConagua(Resource):

    def get(self):
        http = urllib3.PoolManager()
        try:
            print("Solicitando datos ....")
            http = urllib3.PoolManager()
            response = http.request(
                "Get",
                "https://smn.conagua.gob.mx/webservices/?method=1",
                headers={
                    "Accept-Encoding": "gzip",
                }
            )
            gzipFile = io.BytesIO(response.data)
            raw_data = gzip.decompress(gzipFile.read())
            json_data = json.loads(raw_data)

            print("Enviando datos...")
            return (json_data, 200)

        except Exception as e:
            return ({
                "Descripcion": "Ha ocurrido un error al momento de solicitar los datos",
            }, 500)
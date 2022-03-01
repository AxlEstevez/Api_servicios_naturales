from .PronosticoSMN import GetDataFromConagua
from .CalidaAire import GetDataAire

def initRouter(api):
    api.add_resource(GetDataFromConagua, '/api/pronostico/get')
    api.add_resource(GetDataAire, '/api/CalidadDelAire/get')
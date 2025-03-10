from geopy.geocoders import Nominatim
import requests
from fake_useragent import UserAgent
import json

class Searcher:
    trash_day_url:str = 'https://apisgi.mosaro.com.br/external/parqueservico/area-coleta/buscar-por-endereco-ou-posicao'
    ua = UserAgent()
    def __init__(self,adress:str=None):
        self.adress:str = adress.replace(" ","+")
        self.session:object = requests.session()

        self.trash_day_info:dict = self._get_trash_day_info()
        self.lat , self.long = self._get_location()

    def _get_location(self) -> float:
        geolocator = Nominatim(user_agent="geoapi")
        location = geolocator.geocode(self.adress)

        if location:
            return location.latitude, location.longitude
        else:
            return "Endereço não encontrado"

    def _get_trash_day_info(self) -> dict:
        params = {
            'count': 1
            , 'cod_parque_servico': 164
            , 'address': self.adress
            , 'is_frame': True
        }
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Origin': 'https://iframesgi-limpeza.mosaro.com.br',
            'Referer': 'https://iframesgi-limpeza.mosaro.com.br/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': self.ua.random,
        }

        response = self.session.get(self.trash_day_url, params=params, headers=headers)
        dados:dict = json.loads(response.text)

        return dados['area_coleta_horario']

if __name__ == '__main__':
    adress = 'Passagem Lindolfo Collor'
    #adress = 'Travessa Francisco Monteiro - 474'
    seacher = Searcher(adress=adress)

    print(seacher.trash_day_info)
    print(seacher.lat , seacher.long)
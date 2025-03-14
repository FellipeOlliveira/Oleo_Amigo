from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
from fake_useragent import UserAgent
import json

class Searcher:
    trash_day_url:str = 'https://apisgi.mosaro.com.br/external/parqueservico/area-coleta/buscar-por-endereco-ou-posicao'
    ua = UserAgent()
    def __init__(self):
        self.session:object = requests.session()

    def get_location(self,address) -> float:
        address_search = address.replace(" ","+")
        geolocator = Nominatim(user_agent="geoapi", timeout=10)
        location = geolocator.geocode(address_search)

        if location is None:
            print(f"Endereço não encontrado: {address}")
            return None, None  # Retorna none para evitar erros

        return location.latitude, location.longitude

    def get_trash_day_info(self,address) -> dict:
        address_search = address.replace(" ", "+")

        params = {
            'count': 1
            , 'cod_parque_servico': 164
            , 'address': address_search
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

        #response = self.session.get(self.trash_day_url, params=params, headers=headers)
        #dados:dict = json.loads(response.text)

        #return dados['area_coleta_horario']

    def get_intersection(self,street1, street2, city):
        coords1 = self.get_location(f"{street1}, {city}")
        coords2 = self.get_location(f"{street2}, {city}")

        if None in (coords1, coords2):
            return None, None  # Retorna None caso uma das ruas n for encontrada

        dist = geodesic(coords1, coords2).meters  # Calcula a distância entre os pontos

        if dist < 500:  # Se estiverem razoavelmente próximos, assumir como cruzamento
            return ((coords1[0] + coords2[0]) / 2, (coords1[1] + coords2[1]) / 2)
        else:
            return None  # Não parece um cruzamento

if __name__ == '__main__':
    adress = 'Dr. Freitas, Marco, Belém - PA'

    street1 = "Av. Almirante Barroso"
    street2 = "Av. Dr. Freitas"
    city = "Marco, Belém - PA"

    #adress = 'Travessa Francisco Monteiro - 474'
    seacher = Searcher()

    print(seacher.get_location(adress))
    #print(seacher.get_intersection(street1=street1,street2=street2,city=city))